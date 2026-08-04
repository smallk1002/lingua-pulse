"""
清空所有课程相关数据（statements → courses → course_packs）
用法：uv run python clear_courses.py
"""
import asyncio
from sqlalchemy import delete as sa_delete
from app.core.database import async_session
from app.models import Statement, Course, CoursePack


async def clear_all():
    async with async_session() as session:
        r1 = await session.execute(sa_delete(Statement))
        r2 = await session.execute(sa_delete(Course))
        r3 = await session.execute(sa_delete(CoursePack))
        await session.commit()
        print(f"已删除：{r1.rowcount} 个句子, {r2.rowcount} 门课程, {r3.rowcount} 个课程包")


if __name__ == "__main__":
    asyncio.run(clear_all())
