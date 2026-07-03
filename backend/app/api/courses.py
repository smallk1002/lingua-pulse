"""
课程 API

GET  /api/course-packs                        公开课程包列表
GET  /api/course-packs/{pack_id}               课程包详情
GET  /api/course-packs/{pack_id}/courses/{c_id} 课程详情（含句子 + 进度）
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.core.security import get_current_user, get_optional_user
from app.models.user import User
from app.models.course import CoursePack, Course, Statement
from app.models.others import MasteredElement, LearningSession
from app.models.progress import CourseProgress
from app.models.review import ReviewItem
from app.schemas.course import (
    CoursePackOut,
    CoursePackDetailOut,
    CourseDetailOut,
    CourseOut,
    StatementOut,
    CourseProgressOut,
)

router = APIRouter(prefix="/api/course-packs", tags=["courses"])


@router.get("", response_model=list[CoursePackOut])
async def list_course_packs(
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    # 基础查询：公开课程包 + 课程数/句子数统计
    base = (
        select(
            CoursePack,
            func.count(func.distinct(Course.id)).label("course_count"),
            func.count(Statement.id).label("statement_count"),
        )
        .outerjoin(Course, Course.course_pack_id == CoursePack.id)
        .outerjoin(Statement, Statement.course_id == Course.id)
        .where(CoursePack.is_public == True)
        .group_by(CoursePack.id)
    )

    if user:
        # 登录用户：综合学习时间（LearningSession 或 CourseProgress，取最新）
        # CourseProgress 每做一题就更新，LearningSession 课程完成时上报
        last_active_sub = (
            select(
                Course.course_pack_id,
                func.max(
                    func.coalesce(
                        LearningSession.created_at,
                        CourseProgress.updated_at,
                    )
                ).label("last_active"),
            )
            .outerjoin(
                LearningSession,
                and_(
                    LearningSession.course_id == Course.id,
                    LearningSession.user_id == user.id,
                ),
            )
            .outerjoin(
                CourseProgress,
                and_(
                    CourseProgress.course_id == Course.id,
                    CourseProgress.user_id == user.id,
                ),
            )
            .where(
                or_(
                    LearningSession.id.isnot(None),
                    CourseProgress.id.isnot(None),
                )
            )
            .group_by(Course.course_pack_id)
        ).subquery("last_active")

        # 断点续学：用户在每个课包内最后学到的那节课
        last_course_sub = (
            select(CourseProgress.course_id)
            .join(Course, Course.id == CourseProgress.course_id)
            .where(
                Course.course_pack_id == CoursePack.id,
                CourseProgress.user_id == user.id,
                CourseProgress.completed_at.is_(None),
                CourseProgress.statement_index > 0,
            )
            .order_by(CourseProgress.statement_index.desc())
            .limit(1)
            .correlate(CoursePack)
        ).scalar_subquery()

        query = (
            base.add_columns(
                last_active_sub.c.last_active,
                last_course_sub.label("last_course_id"),
            )
            .outerjoin(
                last_active_sub,
                last_active_sub.c.course_pack_id == CoursePack.id,
            )
            .group_by(CoursePack.id, last_active_sub.c.last_active)
            .order_by(
                last_active_sub.c.last_active.desc().nulls_last(),
                CoursePack.created_at.desc(),
            )
        )
    else:
        # 未登录：按创建时间降序
        query = base.order_by(CoursePack.created_at.desc())

    result = await db.execute(query)
    rows = result.all()

    packs = []
    for row in rows:
        pack = row[0]
        course_count = row[1]
        statement_count = row[2]
        last_active = row[3] if len(row) > 3 and row[3] is not None else None
        last_course_id = row[4] if len(row) > 4 and row[4] is not None else None
        p = CoursePackOut.model_validate(pack)
        p.course_count = course_count
        p.statement_count = statement_count
        p.last_active = last_active
        p.last_course_id = last_course_id
        packs.append(p)
    return packs


@router.get("/{pack_id}", response_model=CoursePackDetailOut)
async def get_course_pack(
    pack_id: str,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    result = await db.execute(
        select(CoursePack)
        .options(selectinload(CoursePack.courses).selectinload(Course.statements))
        .where(CoursePack.id == pack_id)
    )
    pack = result.scalar_one_or_none()
    if not pack:
        raise HTTPException(status_code=404, detail="课程包不存在")

    # 断点续学：查找用户在该课包内最后学到的那节课
    last_course_id: str | None = None
    if user:
        prog_result = await db.execute(
            select(CourseProgress.course_id)
            .join(Course, Course.id == CourseProgress.course_id)
            .where(
                Course.course_pack_id == pack_id,
                CourseProgress.user_id == user.id,
                CourseProgress.completed_at.is_(None),
                CourseProgress.statement_index > 0,
            )
            .order_by(CourseProgress.statement_index.desc())
            .limit(1)
        )
        row = prog_result.one_or_none()
        if row:
            last_course_id = row[0]

    # 统计
    course_count = len(pack.courses)
    statement_count = sum(len(c.statements) for c in pack.courses)

    return CoursePackDetailOut(
        id=pack.id,
        title=pack.title,
        description=pack.description,
        cover_url=pack.cover_url,
        difficulty=pack.difficulty,
        is_public=pack.is_public,
        creator_id=pack.creator_id,
        created_at=pack.created_at,
        course_count=course_count,
        statement_count=statement_count,
        last_course_id=last_course_id,
        courses=[CourseOut.model_validate(c) for c in pack.courses],
    )


@router.get("/{pack_id}/courses/{course_id}", response_model=CourseDetailOut)
async def get_course_detail(
    pack_id: str,
    course_id: str,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    result = await db.execute(
        select(Course)
        .options(selectinload(Course.statements))
        .where(Course.id == course_id, Course.course_pack_id == pack_id)
    )
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="课程不存在")

    # 查询进度（仅登录用户）
    progress = None
    if user:
        prog_result = await db.execute(
            select(CourseProgress).where(
                CourseProgress.user_id == user.id,
                CourseProgress.course_id == course_id,
            )
        )
        prog = prog_result.scalar_one_or_none()
        if prog:
            progress = CourseProgressOut.model_validate(prog)

    # 查询已掌握的句子 ID（过滤用）
    mastered_ids = set()
    if user:
        master_result = await db.execute(
            select(MasteredElement.statement_id).where(
                MasteredElement.user_id == user.id,
                MasteredElement.statement_id.in_([s.id for s in course.statements]),
            )
        )
        mastered_ids = {row[0] for row in master_result.all()}

    # 过滤掉已掌握的句子
    visible_statements = [
        StatementOut.model_validate(s)
        for s in course.statements
        if s.id not in mastered_ids
    ]

    return CourseDetailOut(
        id=course.id,
        title=course.title,
        description=course.description,
        order=course.order,
        difficulty=course.difficulty,
        created_at=course.created_at,
        statements=visible_statements,
        progress=progress,
    )
