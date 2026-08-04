"""
种子数据导入脚本

从内嵌数据文件导入课程内容，无需外部依赖。

数据源：
- app/data/xingrong.py → 星荣零基础学英语 (55 课)
- app/data/nce1.py      → 新概念英语第一册 (30 课)
- app/data/nce2.py      → 新概念英语第二册 (20 课)
- app/data/nce3.py      → 新概念英语第三册 (15 课)
- app/data/nce4.py      → 新概念英语第四册 (15 课)

用法：uv run python seed.py
"""

import asyncio
import uuid

from sqlalchemy import select, delete as sa_delete

from app.core.database import async_session
from app.models import CoursePack, Course, Statement
from app.data.xingrong import XINGRONG_COURSES
from app.data.nce1 import NCE1_COURSES
from app.data.nce2 import NCE2_COURSES
from app.data.nce3 import NCE3_COURSES
from app.data.nce4 import NCE4_COURSES


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
        "difficulty": "beginner",
        "courses": NCE1_COURSES,
    },
    {
        "title": "新概念英语第二册",
        "description": "实践与进步，短文阅读与过去时态练习。",
        "difficulty": "intermediate",
        "courses": NCE2_COURSES,
    },
    {
        "title": "新概念英语第三册",
        "description": "培养技能，复杂句型与段落理解训练。",
        "difficulty": "advanced",
        "courses": NCE3_COURSES,
    },
    {
        "title": "新概念英语第四册",
        "description": "流利英语，学术思辨与高阶表达。",
        "difficulty": "advanced",
        "courses": NCE4_COURSES,
    },
]


async def seed_course_pack(title, description, difficulty, courses):
    total = 0
    async with async_session() as session:
        result = await session.execute(
            select(CoursePack).where(CoursePack.title == title)
        )
        existing = result.scalar_one_or_none()
        if existing:
            print(f"  ⏭ 已存在：{title}，清空旧数据")
            pack_id = existing.id
            subq = select(Course.id).where(Course.course_pack_id == pack_id)
            await session.execute(sa_delete(Statement).where(Statement.course_id.in_(subq)))
            await session.execute(sa_delete(Course).where(Course.course_pack_id == pack_id))
            await session.commit()
        else:
            pack_id = str(uuid.uuid4())
            session.add(CoursePack(id=pack_id, title=title, description=description, difficulty=difficulty, is_public=True))
            await session.commit()

    for i, c in enumerate(courses):
        async with async_session() as session:
            cid = str(uuid.uuid4())
            session.add(Course(id=cid, title=c["title"], order=i + 1, difficulty=difficulty, course_pack_id=pack_id))
            await session.flush()
            for j, s in enumerate(c["statements"]):
                kw = {"id": str(uuid.uuid4()), "order": j + 1, "chinese": s["chinese"], "english": s["english"], "soundmark": s.get("soundmark"), "course_id": cid}
                if s.get("grammar"):
                    kw["grammar"] = s["grammar"]
                session.add(Statement(**kw))
                total += 1
            await session.commit()
        print(f"  ✓ {c['title']}：{len(c['statements'])} 句")
    return len(courses), total


async def main():
    print("=" * 60)
    print("LinguaPulse 种子数据导入")
    print("=" * 60)
    print()
    gc, gs = 0, 0
    for p in COURSE_PACKS:
        print(f"📦 {p['title']}")
        nc, ns = await seed_course_pack(p["title"], p["description"], p["difficulty"], p["courses"])
        print(f"  ✅ {nc} 课, {ns} 句\n")
        gc += nc
        gs += ns
    print("=" * 60)
    print(f"🎉 完成！{len(COURSE_PACKS)} 个课程包, {gc} 课, {gs} 句")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
