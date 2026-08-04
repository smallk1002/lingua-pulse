"""
游戏 & 复习 API

POST /api/game/check           提交答案检查
POST /api/review/submit        提交 SM-2 复习评分
GET  /api/review/due           获取待复习句子
PUT  /api/review/{id}/master   标记/取消掌握
"""

import uuid
from datetime import datetime, date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user, get_optional_user
from app.models.user import User
from app.models.course import Statement
from app.models.review import ReviewItem
from app.models.others import MasteredElement, UserStats
from app.schemas.game import (
    AnswerSubmit,
    AnswerResult,
    ReviewSubmit,
    ReviewItemOut,
    MasterToggle,
)
from app.schemas.course import ProgressUpdate
from app.services.game_engine import (
    check_answer,
    calc_quality,
    calc_xp,
    sm2_algorithm,
    normalize_text,
)

router = APIRouter(tags=["game"])


@router.post("/api/game/check", response_model=AnswerResult)
async def submit_answer(
    data: AnswerSubmit,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """检查用户提交的答题结果（游客也可使用，但不计统计）"""
    # 获取句子
    result = await db.execute(select(Statement).where(Statement.id == data.statement_id))
    stmt = result.scalar_one_or_none()
    if not stmt:
        raise HTTPException(status_code=404, detail="句子不存在")

    # 逐词检查
    check_result = check_answer(data.user_input, stmt.english)
    quality = calc_quality(data.fix_count, data.difficulty)

    # 统计仅对已登录用户更新
    xp = 0
    if user and data.fix_count == 0:
        xp = calc_xp(quality, combo=0, is_review=False, is_first_of_day=False)
        stats_result = await db.execute(
            select(UserStats).where(UserStats.user_id == user.id)
        )
        stats = stats_result.scalar_one_or_none()
        if stats:
            today = date.today()
            if stats.last_study_date != today:
                if stats.last_study_date and (today - stats.last_study_date).days == 1:
                    stats.streak += 1
                elif stats.last_study_date and (today - stats.last_study_date).days > 1:
                    stats.streak = 1
                else:
                    stats.streak = max(stats.streak, 1)
                stats.longest_streak = max(stats.longest_streak, stats.streak)
                stats.last_study_date = today
            stats.xp += xp
            stats.total_statements += 1
            stats.level = int((stats.xp / 100) ** 0.5) + 1

    await db.commit()

    return AnswerResult(
        correct=check_result["correct"],
        incorrect_words=check_result["incorrect_words"],
        normalized_input=normalize_text(data.user_input),
        quality=quality,
        xp_earned=xp,
    )


@router.post("/api/review/submit", response_model=ReviewItemOut)
async def submit_review(
    data: ReviewSubmit,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """提交 SM-2 复习评分（答题通过后调用）"""
    # 查找或创建 ReviewItem
    result = await db.execute(
        select(ReviewItem).where(
            and_(
                ReviewItem.user_id == user.id,
                ReviewItem.statement_id == data.statement_id,
            )
        )
    )
    item = result.scalar_one_or_none()

    if not item:
        item = ReviewItem(
            id=str(uuid.uuid4()),
            user_id=user.id,
            statement_id=data.statement_id,
        )
        db.add(item)
        await db.flush()

    # 执行 SM-2 算法
    sm2_algorithm(data.quality, item)
    await db.commit()
    await db.refresh(item)

    return ReviewItemOut.model_validate(item)


@router.get("/api/review/due", response_model=list[ReviewItemOut])
async def get_due_reviews(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """获取当前用户所有到期待复习的句子"""
    result = await db.execute(
        select(ReviewItem)
        .where(
            and_(
                ReviewItem.user_id == user.id,
                ReviewItem.next_review_at <= datetime.utcnow(),
            )
        )
        .order_by(ReviewItem.next_review_at.asc())
        .limit(50)
    )
    items = result.scalars().all()
    return [ReviewItemOut.model_validate(item) for item in items]


@router.put("/api/review/{statement_id}/master")
async def toggle_master(
    statement_id: str,
    data: MasterToggle,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """标记或取消标记句子为已掌握"""
    if data.mastered:
        # 检查是否已标记
        result = await db.execute(
            select(MasteredElement).where(
                and_(
                    MasteredElement.user_id == user.id,
                    MasteredElement.statement_id == statement_id,
                )
            )
        )
        if not result.scalar_one_or_none():
            master = MasteredElement(
                id=str(uuid.uuid4()),
                user_id=user.id,
                statement_id=statement_id,
            )
            db.add(master)
    else:
        # 取消标记
        result = await db.execute(
            select(MasteredElement).where(
                and_(
                    MasteredElement.user_id == user.id,
                    MasteredElement.statement_id == statement_id,
                )
            )
        )
        item = result.scalar_one_or_none()
        if item:
            await db.delete(item)

    await db.commit()
    return {"mastered": data.mastered}


@router.put("/api/progress/{course_id}")
async def update_progress(
    course_id: str,
    data: ProgressUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """断点续学：更新课程进度"""
    from app.models.progress import CourseProgress

    result = await db.execute(
        select(CourseProgress).where(
            and_(
                CourseProgress.user_id == user.id,
                CourseProgress.course_id == course_id,
            )
        )
    )
    prog = result.scalar_one_or_none()

    if prog:
        prog.statement_index = data.statement_index
    else:
        prog = CourseProgress(
            id=str(uuid.uuid4()),
            user_id=user.id,
            course_id=course_id,
            statement_index=data.statement_index,
        )
        db.add(prog)

    await db.commit()
    return {"statement_index": data.statement_index}


@router.post("/api/progress/{course_id}/complete")
async def complete_course(
    course_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """完成一课"""
    from app.models.progress import CourseProgress, CourseHistory
    from app.models.course import Course

    # 更新进度
    result = await db.execute(
        select(CourseProgress).where(
            and_(
                CourseProgress.user_id == user.id,
                CourseProgress.course_id == course_id,
            )
        )
    )
    prog = result.scalar_one_or_none()
    if prog:
        prog.completed_at = datetime.utcnow()

    # 更新或创建完成历史
    hist_result = await db.execute(
        select(CourseHistory).where(
            and_(
                CourseHistory.user_id == user.id,
                CourseHistory.course_id == course_id,
            )
        )
    )
    hist = hist_result.scalar_one_or_none()

    # 获取 course_pack_id
    course_result = await db.execute(select(Course).where(Course.id == course_id))
    course = course_result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="课程不存在")

    # 查找下一课（幂等路径也要返回，所以提前查）
    next_result = await db.execute(
        select(Course)
        .where(
            and_(
                Course.course_pack_id == course.course_pack_id,
                Course.order > course.order,
            )
        )
        .order_by(Course.order.asc())
        .limit(1)
    )
    next_course = next_result.scalar_one_or_none()

    if hist:
        # 已经完成过，不重复加 XP（幂等）
        hist.last_completed_at = datetime.utcnow()
        await db.commit()
        return {
            "completed": True,
            "xp_awarded": 0,
            "already_completed": True,
            "next_course_id": next_course.id if next_course else None,
            "next_course_title": next_course.title if next_course else None,
        }

    # 首次完成
    hist = CourseHistory(
        id=str(uuid.uuid4()),
        user_id=user.id,
        course_id=course_id,
        course_pack_id=course.course_pack_id,
        completion_count=1,
    )
    db.add(hist)

    # 课程完成 XP
    stats_result = await db.execute(
        select(UserStats).where(UserStats.user_id == user.id)
    )
    stats = stats_result.scalar_one_or_none()
    if stats:
        stats.xp += 50
        stats.level = int((stats.xp / 100) ** 0.5) + 1

    await db.commit()

    return {
        "completed": True,
        "xp_awarded": 50,
        "next_course_id": next_course.id if next_course else None,
        "next_course_title": next_course.title if next_course else None,
    }
