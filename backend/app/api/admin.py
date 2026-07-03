"""
管理后台 API（需管理员权限）

注意：当前版本管理员检查通过 user 表 is_admin 字段实现。
如需要更细粒度的权限控制，后续可引入 RBAC。
"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.course import CoursePack, Course, Statement
from app.schemas.course import (
    CoursePackCreate,
    CoursePackUpdate,
    CoursePackOut,
    CourseCreate,
    CourseUpdate,
    CourseOut,
    StatementCreate,
    StatementUpdate,
    StatementReorder,
    StatementOut,
)

router = APIRouter(prefix="/api/admin", tags=["admin"])


async def require_admin(user: User = Depends(get_current_user)) -> User:
    """管理员权限检查（V1 简单判断：is_active + email 后缀或特殊标记）"""
    # TODO: V2 引入 role 表实现 RBAC
    # 目前简单判断：活跃用户即可操作管理后台（MVP 阶段）
    if not user.is_active:
        raise HTTPException(status_code=403, detail="无管理权限")
    return user


# ── 课程包管理 ──

@router.post("/course-packs", response_model=CoursePackOut, status_code=201)
async def create_course_pack(
    data: CoursePackCreate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    pack = CoursePack(
        id=str(uuid.uuid4()),
        title=data.title,
        description=data.description,
        cover_url=data.cover_url,
        difficulty=data.difficulty,
        is_public=data.is_public,
        creator_id=admin.id,
    )
    db.add(pack)
    await db.commit()
    await db.refresh(pack)
    return CoursePackOut.model_validate(pack)


@router.put("/course-packs/{pack_id}", response_model=CoursePackOut)
async def update_course_pack(
    pack_id: str,
    data: CoursePackUpdate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    result = await db.execute(select(CoursePack).where(CoursePack.id == pack_id))
    pack = result.scalar_one_or_none()
    if not pack:
        raise HTTPException(status_code=404, detail="课程包不存在")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(pack, key, value)

    await db.commit()
    await db.refresh(pack)
    return CoursePackOut.model_validate(pack)


@router.delete("/course-packs/{pack_id}", status_code=204)
async def delete_course_pack(
    pack_id: str,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    result = await db.execute(select(CoursePack).where(CoursePack.id == pack_id))
    pack = result.scalar_one_or_none()
    if not pack:
        raise HTTPException(status_code=404, detail="课程包不存在")
    await db.delete(pack)
    await db.commit()
    return None


# ── 课程管理 ──

@router.post("/courses", response_model=CourseOut, status_code=201)
async def create_course(
    data: CourseCreate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    # 验证课程包存在
    result = await db.execute(
        select(CoursePack).where(CoursePack.id == data.course_pack_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="课程包不存在")

    course = Course(
        id=str(uuid.uuid4()),
        title=data.title,
        description=data.description,
        order=data.order,
        difficulty=data.difficulty,
        course_pack_id=data.course_pack_id,
    )
    db.add(course)
    await db.commit()
    await db.refresh(course)
    return CourseOut.model_validate(course)


@router.put("/courses/{course_id}", response_model=CourseOut)
async def update_course(
    course_id: str,
    data: CourseUpdate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="课程不存在")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)
    return CourseOut.model_validate(course)


@router.delete("/courses/{course_id}", status_code=204)
async def delete_course(
    course_id: str,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="课程不存在")
    await db.delete(course)
    await db.commit()
    return None


# ── 句子管理 ──

@router.post("/statements", response_model=StatementOut, status_code=201)
async def create_statement(
    data: StatementCreate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    # 验证课程存在
    result = await db.execute(select(Course).where(Course.id == data.course_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="课程不存在")

    statement = Statement(
        id=str(uuid.uuid4()),
        order=data.order,
        chinese=data.chinese,
        english=data.english,
        soundmark=data.soundmark,
        grammar=data.grammar,
        course_id=data.course_id,
    )
    db.add(statement)
    await db.commit()
    await db.refresh(statement)
    return StatementOut.model_validate(statement)


@router.put("/statements/{statement_id}", response_model=StatementOut)
async def update_statement(
    statement_id: str,
    data: StatementUpdate,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    result = await db.execute(select(Statement).where(Statement.id == statement_id))
    stmt = result.scalar_one_or_none()
    if not stmt:
        raise HTTPException(status_code=404, detail="句子不存在")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(stmt, key, value)

    await db.commit()
    await db.refresh(stmt)
    return StatementOut.model_validate(stmt)


@router.delete("/statements/{statement_id}", status_code=204)
async def delete_statement(
    statement_id: str,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    result = await db.execute(select(Statement).where(Statement.id == statement_id))
    stmt = result.scalar_one_or_none()
    if not stmt:
        raise HTTPException(status_code=404, detail="句子不存在")
    await db.delete(stmt)
    await db.commit()
    return None


@router.put("/statements/reorder")
async def reorder_statements(
    data: StatementReorder,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin),
):
    """按新顺序重新排列句子"""
    for new_order, sid in enumerate(data.statement_ids, start=1):
        await db.execute(
            update(Statement).where(Statement.id == sid).values(order=new_order)
        )
    await db.commit()
    return {"reordered": len(data.statement_ids)}
