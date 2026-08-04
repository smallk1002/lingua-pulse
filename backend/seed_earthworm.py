"""
种子数据导入 — earthworm 格式

从 app/data/earthworm/ 目录读取 earthworm 风格的课程 JSON 文件，
导入到 CoursePack → Course → Statement 三层结构。

目录结构：
  app/data/earthworm/
    courses/     → 星荣零基础学英语 (01.json ~ 60.json)
    nce1/        → 新概念英语第一册 (01.json ~ 70.json)
    nce2/        → 新概念英语第二册 (01.json ~ 90.json)
    nce3/        → 新概念英语第三册 (01.json ~ 60.json)
    nce4/        → 新概念英语第四册 (01.json ~ 50.json)
    cet4/        → 大学英语四级 (01.json ~ 30.json)

用法：uv run python seed_earthworm.py
"""

import asyncio
import json
import os
import uuid

from sqlalchemy import select, delete as sa_delete

from app.core.database import async_session
from app.models import CoursePack, Course, Statement


BASE_DIR = os.path.join(os.path.dirname(__file__), "app", "data", "earthworm")

COURSE_PACKS = [
    {
        "dir": "courses",
        "title": "星荣零基础学英语",
        "description": "最适合零基础入门的英语课程，从单词到句子循序渐进。",
        "difficulty": "beginner",
    },
    {
        "dir": "nce1",
        "title": "新概念英语第一册",
        "description": "新概念英语第一册经典教材，涵盖基础语法与日常对话。",
        "difficulty": "beginner",
    },
    {
        "dir": "nce2",
        "title": "新概念英语第二册",
        "description": "实践与进步，短文阅读与过去时态练习。",
        "difficulty": "intermediate",
    },
    {
        "dir": "nce3",
        "title": "新概念英语第三册",
        "description": "培养技能，复杂句型与段落理解训练。",
        "difficulty": "advanced",
    },
    {
        "dir": "nce4",
        "title": "新概念英语第四册",
        "description": "流利英语，学术思辨与高阶表达。",
        "difficulty": "advanced",
    },
    {
        "dir": "cet4",
        "title": "大学英语四级 (CET-4)",
        "description": "覆盖 CET-4 高频词汇、核心语法与考试场景，30 课助你轻松过四级。",
        "difficulty": "intermediate",
    },
]


def convert_chinese_number(num: int) -> str:
    """将数字转换为中文课名，如 1 → 第一课, 12 → 第十二课"""
    if num < 1:
        return f"第{num}课"
    chinese_numbers = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    if num <= 10:
        return f"第{chinese_numbers[num]}课"
    elif num < 20:
        return f"第十{chinese_numbers[num - 10]}课"
    elif num < 100:
        tens = num // 10
        ones = num % 10
        if ones == 0:
            return f"第{chinese_numbers[tens]}十课"
        return f"第{chinese_numbers[tens]}十{chinese_numbers[ones]}课"
    return f"第{num}课"


async def seed_course_pack(pack_config: dict) -> tuple[int, int]:
    """导入一个课程包的所有课程"""
    dir_path = os.path.join(BASE_DIR, pack_config["dir"])
    if not os.path.isdir(dir_path):
        print(f"  ⚠ 目录不存在: {dir_path}")
        return 0, 0

    # 读取所有 JSON 文件并按文件名排序
    files = sorted(
        [f for f in os.listdir(dir_path) if f.endswith(".json")],
        key=lambda x: int(x.replace(".json", "")) if x.replace(".json", "").isdigit() else 0,
    )

    if not files:
        print(f"  ⚠ 目录为空: {dir_path}")
        return 0, 0

    pack_id: str
    async with async_session() as session:
        # 检查是否已有同名课程包
        result = await session.execute(
            select(CoursePack).where(CoursePack.title == pack_config["title"])
        )
        existing = result.scalar_one_or_none()
        if existing:
            pack_id = existing.id
            # 清空旧数据
            subq = select(Course.id).where(Course.course_pack_id == pack_id)
            await session.execute(sa_delete(Statement).where(Statement.course_id.in_(subq)))
            await session.execute(sa_delete(Course).where(Course.course_pack_id == pack_id))
            await session.commit()
            print(f"  🔄 已存在，清空旧数据")
        else:
            pack_id = str(uuid.uuid4())
            session.add(CoursePack(
                id=pack_id,
                title=pack_config["title"],
                description=pack_config["description"],
                difficulty=pack_config["difficulty"],
                is_public=True,
            ))
            await session.commit()

    total_courses = 0
    total_statements = 0

    for order, filename in enumerate(files):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            statements_data = json.load(f)

        if not isinstance(statements_data, list):
            print(f"  ⚠ {filename} 格式异常，跳过")
            continue

        course_num = int(filename.replace(".json", ""))
        course_title = convert_chinese_number(course_num)

        async with async_session() as session:
            course_id = str(uuid.uuid4())
            session.add(Course(
                id=course_id,
                title=course_title,
                order=order + 1,
                difficulty=pack_config["difficulty"],
                course_pack_id=pack_id,
            ))
            await session.flush()

            stmt_count = 0
            for i, stmt in enumerate(statements_data):
                if not stmt.get("english"):
                    continue
                session.add(Statement(
                    id=str(uuid.uuid4()),
                    order=i + 1,
                    chinese=stmt.get("chinese", ""),
                    english=stmt["english"],
                    soundmark=stmt.get("soundmark"),
                    grammar=stmt.get("grammar"),
                    course_id=course_id,
                ))
                stmt_count += 1

            await session.commit()
            total_courses += 1
            total_statements += stmt_count
            print(f"  ✓ {course_title}（{filename}）：{stmt_count} 句")

    return total_courses, total_statements


async def main():
    print("=" * 60)
    print("LinguaPulse 种子数据导入 (earthworm 格式)")
    print("=" * 60)
    print()

    grand_courses = 0
    grand_statements = 0

    for pack in COURSE_PACKS:
        print(f"📦 {pack['title']}")
        nc, ns = await seed_course_pack(pack)
        print(f"  ✅ {nc} 课, {ns} 句\n")
        grand_courses += nc
        grand_statements += ns

    print("=" * 60)
    print(f"🎉 完成！{len(COURSE_PACKS)} 个课程包, {grand_courses} 课, {grand_statements} 句")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
