"""
种子数据导入脚本

从内嵌数据文件导入课程内容，无需外部依赖。

数据源：
- app/data/xingrong.py → 课程包「星荣零基础学英语」(20 课)
- app/data/nce.py      → 课程包「新概念英语第一册」(10 课)

用法：uv run python seed.py
"""

import asyncio
import uuid

from sqlalchemy import select, delete as sa_delete

from app.core.database import async_session
from app.models import CoursePack, Course, Statement
from app.data.xingrong import XINGRONG_COURSES
from app.data.nce import NCE_COURSES


# ── 课程包配置 ──
COURSE_PACKS = [
    {
        "title": "星荣零基础学英语",
        "description": "最适合零基础入门的英语课程，从单词到句子循序渐进。",
        "difficulty": "beginner",
        "courses": XINGRONG_COURSES,
    },
    {
        "title": "新概念英语第一册",
        "description": "新概念英语第一册经典教材，涵盖基础语法与日常对话。",
        "difficulty": "intermediate",
        "courses": NCE_COURSES,
    },
]


async def seed_course_pack(
    title: str,
    description: str,
    difficulty: str,
    courses: list[dict],
) -> tuple[int, int]:
    """
    创建课程包并导入全部课程数据。
    如果课程包已存在，先清空旧数据再重新导入。
    返回 (课程数, 句子数)。
    """
    async with async_session() as session:
        # 检查是否已存在
        result = await session.execute(
            select(CoursePack).where(CoursePack.title == title)
        )
        existing = result.scalar_one_or_none()

        if existing:
            print(f"  ⏭ 课程包已存在：{title}，清空旧数据后重新导入")
            pack_id = existing.id
            # 先删 statements，再删 courses
            subq = select(Course.id).where(Course.course_pack_id == pack_id)
            await session.execute(sa_delete(Statement).where(Statement.course_id.in_(subq)))
            await session.execute(sa_delete(Course).where(Course.course_pack_id == pack_id))
            await session.commit()
        else:
            pack_id = str(uuid.uuid4())
            pack = CoursePack(
                id=pack_id,
                title=title,
                description=description,
                difficulty=difficulty,
                is_public=True,
            )
            session.add(pack)
            await session.commit()

    # 逐课导入
    total_statements = 0
    for course_idx, course_data in enumerate(courses):
        course_title = course_data["title"]
        statements = course_data["statements"]

        async with async_session() as session:
            course_id = str(uuid.uuid4())
            course = Course(
                id=course_id,
                title=course_title,
                description=None,
                order=course_idx + 1,
                difficulty=difficulty,
                course_pack_id=pack_id,
            )
            session.add(course)
            await session.flush()

            for order_idx, stmt in enumerate(statements):
                stmt_kwargs = {
                    "id": str(uuid.uuid4()),
                    "order": order_idx + 1,
                    "chinese": stmt["chinese"],
                    "english": stmt["english"],
                    "soundmark": stmt.get("soundmark"),
                    "course_id": course_id,
                }
                if stmt.get("grammar"):
                    stmt_kwargs["grammar"] = stmt["grammar"]
                statement = Statement(**stmt_kwargs)
                session.add(statement)
                total_statements += 1

            await session.commit()

        print(f"  ✓ {course_title}：{len(statements)} 个句子")

    return len(courses), total_statements


async def main():
    print("=" * 60)
    print("LinguaPulse 种子数据导入")
    print("=" * 60)
    print()

    grand_total_courses = 0
    grand_total_statements = 0

    for pack in COURSE_PACKS:
        print(f"📦 课程包：{pack['title']}")
        num_courses, num_stmts = await seed_course_pack(
            title=pack["title"],
            description=pack["description"],
            difficulty=pack["difficulty"],
            courses=pack["courses"],
        )
        print(f"  ✅ 共 {num_courses} 课，{num_stmts} 个句子\n")
        grand_total_courses += num_courses
        grand_total_statements += num_stmts

    print("=" * 60)
    print(f"🎉 全部完成！共 {len(COURSE_PACKS)} 个课程包，{grand_total_courses} 课，{grand_total_statements} 个句子")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
