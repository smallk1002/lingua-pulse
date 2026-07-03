"""
TTS、设置、统计 API

POST /api/tts/generate        生成单个 TTS
POST /api/tts/generate-batch   批量生成
GET  /api/tts/audio/{filename} 获取音频文件
GET  /api/settings             获取设置
PUT  /api/settings             更新设置
GET  /api/stats/summary        学习概览
GET  /api/stats/daily          每日统计
POST /api/stats/session        上报学习时长
"""

import os
from datetime import date, datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings as app_settings
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.others import UserSettings, UserStats, LearningSession
from app.models.course import Statement
from app.schemas.others import (
    TTSGenerateRequest,
    TTSGenerateResponse,
    TTSBatchRequest,
    TTSBatchResponse,
    TTSBatchItem,
    SettingsOut,
    SettingsUpdate,
    StatsSummaryOut,
    DailyStatsOut,
    SessionReport,
)
from app.services.tts_service import generate_audio

router = APIRouter(tags=["tts", "settings", "stats"])


# ── TTS ──

@router.post("/api/tts/generate", response_model=TTSGenerateResponse)
async def tts_generate(
    data: TTSGenerateRequest,
    user: User = Depends(get_current_user),
):
    url = await generate_audio(data.text, data.voice, data.speed)
    return TTSGenerateResponse(url=url)


@router.post("/api/tts/generate-batch", response_model=TTSBatchResponse)
async def tts_generate_batch(
    data: TTSBatchRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """批量生成 TTS（用于管理后台）"""
    result = await db.execute(
        select(Statement).where(Statement.id.in_(data.statement_ids))
    )
    statements = result.scalars().all()

    items = []
    for stmt in statements:
        url = await generate_audio(stmt.english, data.voice)
        items.append(TTSBatchItem(statement_id=stmt.id, url=url))

    return TTSBatchResponse(results=items)


@router.get("/api/tts/synthesize")
async def tts_synthesize(
    text: str = Query(..., min_length=1, description="要合成的英文文本"),
    voice: str = Query("en-US-JennyNeural", description="语音角色"),
    speed: str = Query("+0%", description="语速"),
):
    """
    直接合成 TTS 音频并返回 MP3 流。
    自动缓存：相同 text+voice+speed 只生成一次。
    前端直接当 <audio> 的 src 使用。
    """
    url = await generate_audio(text, voice, speed)
    filename = url.rsplit("/", 1)[-1]
    filepath = os.path.join(app_settings.AUDIO_DIR, filename)
    return FileResponse(filepath, media_type="audio/mpeg")


@router.get("/api/tts/audio/{filename}")
async def tts_audio(filename: str):
    """获取缓存音频文件"""
    filepath = os.path.join(app_settings.AUDIO_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="音频文件不存在")
    return FileResponse(filepath, media_type="audio/mpeg")


# ── 设置 ──

@router.get("/api/settings", response_model=SettingsOut)
async def get_settings(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(UserSettings).where(UserSettings.user_id == user.id)
    )
    settings = result.scalar_one_or_none()
    if not settings:
        raise HTTPException(status_code=404, detail="设置不存在")
    return SettingsOut.model_validate(settings)


@router.put("/api/settings", response_model=SettingsOut)
async def update_settings(
    data: SettingsUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(UserSettings).where(UserSettings.user_id == user.id)
    )
    settings = result.scalar_one_or_none()
    if not settings:
        raise HTTPException(status_code=404, detail="设置不存在")

    # 仅更新传入的字段
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(settings, key, value)

    await db.commit()
    await db.refresh(settings)
    return SettingsOut.model_validate(settings)


# ── 统计 ──

@router.get("/api/stats/summary", response_model=StatsSummaryOut)
async def get_stats_summary(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(UserStats).where(UserStats.user_id == user.id)
    )
    stats = result.scalar_one_or_none()
    if not stats:
        raise HTTPException(status_code=404, detail="统计数据不存在")

    xp_to_next = ((stats.level) ** 2) * 100 - stats.xp
    return StatsSummaryOut(
        xp=stats.xp,
        level=stats.level,
        streak=stats.streak,
        longest_streak=stats.longest_streak,
        total_statements=stats.total_statements,
        total_duration=stats.total_duration,
        xp_to_next_level=max(0, xp_to_next),
    )


@router.get("/api/stats/daily", response_model=list[DailyStatsOut])
async def get_daily_stats(
    days: int = Query(default=7, ge=1, le=30),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """获取最近 N 天每日学习统计"""
    result = await db.execute(
        select(LearningSession)
        .where(
            and_(
                LearningSession.user_id == user.id,
                LearningSession.date >= date.today().replace(day=1),
            )
        )
        .order_by(LearningSession.date.desc())
        .limit(days)
    )
    sessions = result.scalars().all()
    return [
        DailyStatsOut(
            date=s.date,
            duration=s.duration,
            statements_count=s.statements_count,
        )
        for s in sessions
    ]


@router.post("/api/stats/session")
async def report_session(
    data: SessionReport,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """上报学习时长（前端每 30 秒调用）"""
    today = date.today()

    # 查找今天的记录
    result = await db.execute(
        select(LearningSession).where(
            and_(
                LearningSession.user_id == user.id,
                LearningSession.date == today,
                LearningSession.course_id == data.course_id,
            )
        )
    )
    session = result.scalar_one_or_none()

    if session:
        session.duration += data.duration
        session.statements_count += data.statements_count
    else:
        session = LearningSession(
            user_id=user.id,
            date=today,
            duration=data.duration,
            statements_count=data.statements_count,
            course_id=data.course_id,
        )
        db.add(session)

    # 同步更新全局统计
    stats_result = await db.execute(
        select(UserStats).where(UserStats.user_id == user.id)
    )
    stats = stats_result.scalar_one_or_none()
    if stats:
        stats.total_duration += data.duration

    await db.commit()
    return {"updated": True}
