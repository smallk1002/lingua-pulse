"""
原地迁移：给数据库中 statements 表的 grammar JSONB 补充 chinese 字段

不删除任何数据，只更新 grammar 列。
保留所有 UUID，学习记录不受影响。

用法：cd backend && uv run python migrate_grammar_chinese.py
"""

import asyncio
import json
import os

from sqlalchemy import select, update

from app.core.database import async_session
from app.models import CoursePack, Course, Statement

BASE_DIR = os.path.join(os.path.dirname(__file__), "app", "data", "earthworm")

COURSE_PACKS = [
    {
        "dir": "courses",
        "title": "星荣零基础学英语",
    },
    {
        "dir": "nce1",
        "title": "新概念英语第一册",
    },
    {
        "dir": "nce2",
        "title": "新概念英语第二册",
    },
    {
        "dir": "nce3",
        "title": "新概念英语第三册",
    },
    {
        "dir": "nce4",
        "title": "新概念英语第四册",
    },
]


async def migrate_pack(pack_config: dict) -> dict:
    """对单个课程包的所有句子原地更新 grammar 字段"""
    dir_path = os.path.join(BASE_DIR, pack_config["dir"])
    if not os.path.isdir(dir_path):
        print(f"  ⚠ 目录不存在: {dir_path}")
        return {"updated": 0, "skipped": 0, "not_found": 0}

    files = sorted(
        [f for f in os.listdir(dir_path) if f.endswith(".json")],
        key=lambda x: int(x.replace(".json", "")) if x.replace(".json", "").isdigit() else 0,
    )

    if not files:
        print(f"  ⚠ 目录为空: {dir_path}")
        return {"updated": 0, "skipped": 0, "not_found": 0}

    updated = 0
    skipped = 0
    not_found = 0

    async with async_session() as session:
        # 1. 找到课程包
        result = await session.execute(
            select(CoursePack).where(CoursePack.title == pack_config["title"])
        )
        pack = result.scalar_one_or_none()
        if not pack:
            print(f"  ⚠ 课程包不存在于数据库: {pack_config['title']}")
            return {"updated": 0, "skipped": 0, "not_found": 0}

        # 2. 找到该课程包下的所有课程，按 order 排序
        result = await session.execute(
            select(Course)
            .where(Course.course_pack_id == pack.id)
            .order_by(Course.order)
        )
        db_courses = result.scalars().all()

        # 按 order 建立索引（order 从 1 开始）
        courses_by_order = {c.order: c for c in db_courses}

        print(f"  📦 课程包: {pack.title} ({len(db_courses)} 课)")

    # 逐课处理
    for order_idx, filename in enumerate(files):
        course_order = order_idx + 1  # seed 时 order = order + 1
        db_course = courses_by_order.get(course_order)

        if not db_course:
            print(f"    ⚠ 数据库中找不到 order={course_order} 的课程，跳过 {filename}")
            not_found += 1
            continue

        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            json_statements = json.load(f)

        if not isinstance(json_statements, list):
            continue

        async with async_session() as session:
            # 3. 读取该课程下的所有数据库 Statement
            result = await session.execute(
                select(Statement)
                .where(Statement.course_id == db_course.id)
                .order_by(Statement.order)
            )
            db_statements = result.scalars().all()

            # 按 english 文本建立索引（一个课程内 english 唯一）
            db_by_english = {s.english.strip().lower(): s for s in db_statements}

            course_updated = 0
            course_skipped = 0

            for json_stmt in json_statements:
                eng = json_stmt.get("english", "").strip().lower()
                if not eng:
                    continue

                db_stmt = db_by_english.get(eng)
                if not db_stmt:
                    # 英文不完全匹配，尝试模糊匹配（去除多余空格）
                    json_eng_normalized = " ".join(eng.split())
                    for s in db_statements:
                        db_normalized = " ".join(s.english.strip().lower().split())
                        if db_normalized == json_eng_normalized:
                            db_stmt = s
                            break

                if not db_stmt:
                    not_found += 1
                    continue

                new_grammar = json_stmt.get("grammar")
                if not new_grammar:
                    course_skipped += 1
                    continue

                # 检查是否需要更新（已有 chinese 字段且和 JSON 一致就跳过）
                old_grammar = db_stmt.grammar
                if old_grammar and isinstance(old_grammar, list):
                    # 比较第一个元素是否有 chinese
                    has_chinese = any(
                        isinstance(g, dict) and g.get("chinese")
                        for g in old_grammar
                    )
                    if has_chinese:
                        # 再检查是否和 JSON 完全一致
                        if old_grammar == new_grammar:
                            course_skipped += 1
                            continue

                # 原地更新
                await session.execute(
                    update(Statement)
                    .where(Statement.id == db_stmt.id)
                    .values(grammar=new_grammar)
                )
                course_updated += 1

            await session.commit()

            if course_updated > 0 or course_skipped > 0:
                course_num = filename.replace(".json", "")
                print(f"    ✓ 第{course_num}课: 更新 {course_updated}, 跳过 {course_skipped}")

            updated += course_updated
            skipped += course_skipped

    return {"updated": updated, "skipped": skipped, "not_found": not_found}


async def main():
    print("=" * 60)
    print("LinguaPulse grammar.chinese 原地迁移")
    print("只更新 grammar 列，不删除任何数据")
    print("=" * 60)
    print()

    total_updated = 0
    total_skipped = 0
    total_not_found = 0

    for pack in COURSE_PACKS:
        print(f"📦 {pack['title']}")
        result = await migrate_pack(pack)
        total_updated += result["updated"]
        total_skipped += result["skipped"]
        total_not_found += result["not_found"]
        print(f"  ✅ 更新 {result['updated']}, 跳过 {result['skipped']}, 未匹配 {result['not_found']}\n")

    print("=" * 60)
    print(f"🎉 完成！")
    print(f"   更新了 {total_updated} 条 Statement 的 grammar 字段")
    print(f"   跳过了 {total_skipped} 条（已有 chinese 或无需更新）")
    if total_not_found > 0:
        print(f"   ⚠ {total_not_found} 条 JSON 数据未在数据库中找到匹配")
    print(f"   所有 UUID 不变，学习记录完整保留 ✓")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
