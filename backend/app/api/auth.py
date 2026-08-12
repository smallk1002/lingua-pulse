"""
认证 API

POST /api/auth/send-code  发送邮箱验证码
POST /api/auth/register   注册（需验证码）
POST /api/auth/login      登录
GET  /api/auth/me         当前用户
"""

import hashlib
import secrets
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.core.security import (
    create_access_token,
    get_current_user,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.models.others import UserSettings, UserStats
from app.models.verification import VerificationCode, LoginAttempt
from app.schemas.auth import (
    SendCodeRequest,
    SendCodeResponse,
    TokenResponse,
    UserLogin,
    UserOut,
    UserRegister,
)
from app.services.email_service import build_code_email, send_email

router = APIRouter(prefix="/api/auth", tags=["auth"])

# ── 防爆破参数 ──
CODE_TTL_MINUTES = 10        # 验证码有效期
CODE_RESEND_SECONDS = 60     # 同邮箱重发间隔
CODE_DAILY_LIMIT = 8         # 同邮箱每天最多发送次数
CODE_IP_HOURLY_LIMIT = 20    # 同 IP 每小时最多发送次数
CODE_MAX_ATTEMPTS = 5        # 单个验证码最多试错次数
LOGIN_MAX_FAILS = 10         # 登录连续失败锁定阈值
LOGIN_LOCK_MINUTES = 15      # 锁定时长


def _hash_code(code: str, email: str) -> str:
    return hashlib.sha256(f"{code}:{email}".encode()).hexdigest()


def _get_client_ip(request: Request) -> str:
    # Nginx 反代后从 X-Forwarded-For 取真实 IP
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def _now() -> datetime:
    return datetime.now(timezone.utc)


@router.post("/send-code", response_model=SendCodeResponse)
async def send_code(
    data: SendCodeRequest, request: Request, db: AsyncSession = Depends(get_db)
):
    email = data.email.lower()
    ip = _get_client_ip(request)
    now = _now()

    # 已注册则无需发码
    result = await db.execute(select(User.id).where(User.email == email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="该邮箱已注册，请直接登录")

    # 限流 1：同邮箱 60 秒内只能发一次
    result = await db.execute(
        select(VerificationCode.created_at)
        .where(VerificationCode.email == email, VerificationCode.purpose == "register")
        .order_by(VerificationCode.created_at.desc())
        .limit(1)
    )
    last = result.scalar_one_or_none()
    if last and (now - last).total_seconds() < CODE_RESEND_SECONDS:
        wait = int(CODE_RESEND_SECONDS - (now - last).total_seconds())
        raise HTTPException(status_code=429, detail=f"发送过于频繁，请 {wait} 秒后重试")

    # 限流 2：同邮箱每天上限
    result = await db.execute(
        select(func.count(VerificationCode.id)).where(
            VerificationCode.email == email,
            VerificationCode.purpose == "register",
            VerificationCode.created_at >= now - timedelta(days=1),
        )
    )
    if result.scalar() >= CODE_DAILY_LIMIT:
        raise HTTPException(status_code=429, detail="今日发送次数已达上限，请明天再试")

    # 限流 3：同 IP 每小时上限
    result = await db.execute(
        select(func.count(VerificationCode.id)).where(
            VerificationCode.ip == ip,
            VerificationCode.created_at >= now - timedelta(hours=1),
        )
    )
    if result.scalar() >= CODE_IP_HOURLY_LIMIT:
        raise HTTPException(status_code=429, detail="操作过于频繁，请稍后再试")

    # 生成 6 位数字验证码
    code = f"{secrets.randbelow(1000000):06d}"

    # 清理该邮箱旧验证码，写入新验证码
    await db.execute(
        delete(VerificationCode).where(
            VerificationCode.email == email, VerificationCode.purpose == "register"
        )
    )
    db.add(
        VerificationCode(
            id=str(uuid.uuid4()),
            email=email,
            purpose="register",
            code_hash=_hash_code(code, email),
            expires_at=now + timedelta(minutes=CODE_TTL_MINUTES),
            ip=ip,
        )
    )
    await db.commit()

    subject, html = build_code_email(settings.APP_NAME, code, CODE_TTL_MINUTES)
    try:
        await send_email(email, subject, html)
    except Exception:
        raise HTTPException(status_code=500, detail="验证码发送失败，请稍后重试")

    return SendCodeResponse(message=f"验证码已发送至 {email}")


@router.post("/register", response_model=TokenResponse, status_code=201)
async def register(data: UserRegister, db: AsyncSession = Depends(get_db)):
    email = data.email.lower()

    # ── 校验验证码 ──
    result = await db.execute(
        select(VerificationCode)
        .where(VerificationCode.email == email, VerificationCode.purpose == "register")
        .order_by(VerificationCode.created_at.desc())
        .limit(1)
    )
    vc = result.scalar_one_or_none()
    if vc is None:
        raise HTTPException(status_code=400, detail="请先获取邮箱验证码")
    if _now() > vc.expires_at:
        raise HTTPException(status_code=400, detail="验证码已过期，请重新获取")
    if vc.attempts >= CODE_MAX_ATTEMPTS:
        raise HTTPException(status_code=400, detail="验证码错误次数过多，请重新获取")
    if vc.code_hash != _hash_code(data.code, email):
        vc.attempts += 1
        await db.commit()
        remain = CODE_MAX_ATTEMPTS - vc.attempts
        raise HTTPException(status_code=400, detail=f"验证码错误，还可尝试 {remain} 次")

    # ── 唯一性检查 ──
    result = await db.execute(select(User).where(User.email == email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="该邮箱已注册")
    result = await db.execute(select(User).where(User.username == data.username))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="该用户名已被占用")

    # ── 创建用户 ──
    user = User(
        id=str(uuid.uuid4()),
        email=email,
        username=data.username,
        password_hash=hash_password(data.password),
    )
    db.add(user)
    await db.flush()

    settings_row = UserSettings(user_id=user.id)
    stats = UserStats(user_id=user.id)
    db.add_all([settings_row, stats])

    # 验证码一次性使用，注册成功后删除
    await db.delete(vc)
    await db.commit()
    await db.refresh(user)

    token = create_access_token(user.id)
    return TokenResponse(access_token=token, user=UserOut.model_validate(user))


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin, db: AsyncSession = Depends(get_db)):
    email = data.email.lower()
    now = _now()

    # ── 锁定检查 ──
    result = await db.execute(select(LoginAttempt).where(LoginAttempt.email == email))
    attempt = result.scalar_one_or_none()
    if attempt and attempt.locked_until and attempt.locked_until > now:
        minutes = int((attempt.locked_until - now).total_seconds() // 60) + 1
        raise HTTPException(
            status_code=429, detail=f"失败次数过多，账号已锁定，请 {minutes} 分钟后重试"
        )

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(data.password, user.password_hash):
        # ── 失败计数 ──
        if attempt is None:
            attempt = LoginAttempt(email=email, fail_count=0)
            db.add(attempt)
        attempt.fail_count += 1
        if attempt.fail_count >= LOGIN_MAX_FAILS:
            attempt.locked_until = now + timedelta(minutes=LOGIN_LOCK_MINUTES)
            attempt.fail_count = 0
            await db.commit()
            raise HTTPException(
                status_code=429,
                detail=f"失败次数过多，账号已锁定 {LOGIN_LOCK_MINUTES} 分钟",
            )
        await db.commit()
        raise HTTPException(status_code=401, detail="邮箱或密码错误")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="账号已禁用")

    # 登录成功，清除失败记录
    if attempt:
        await db.delete(attempt)
        await db.commit()

    token = create_access_token(user.id)
    return TokenResponse(access_token=token, user=UserOut.model_validate(user))


@router.get("/me", response_model=UserOut)
async def get_me(user: User = Depends(get_current_user)):
    return UserOut.model_validate(user)
