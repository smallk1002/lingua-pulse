"""
种子数据导入脚本

从 Earthworm 的 xingrong-courses JSON 文件中读取课程数据，
导入到 LinguaPulse 数据库。

数据源：
- data/courses/*.json  → 课程包「星荣零基础学英语」(55 课)
- data/nce-book1/*.json → 课程包「新概念英语第一册」(10 课)

用法：uv run python seed.py
"""

import asyncio
import json
import os
import uuid
from pathlib import Path

from sqlalchemy import select

from app.core.database import async_session
from app.models import (
    CoursePack,
    Course,
    Statement,
)

# ── 配置 ──
EARTHWORM_COURSES = Path(
    os.environ.get(
        "EARTHWORM_COURSES_PATH",
        "/Users/smallk/www/github/earthworm/packages/xingrong-courses",
    )
)
COURSES_DIR = EARTHWORM_COURSES / "data" / "courses"
NCE_DIR = EARTHWORM_COURSES / "data" / "nce-book1"


# ── 工具函数 ──
def convert_to_chinese_number(num_str: str) -> str:
    """将纯数字文件名转为「第X课」格式，兼容 Earthworm 的命名规则"""
    chinese_numbers = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    n = int(num_str)
    chinese_str = "第"
    if n >= 10:
        tens = n // 10
        ones = n % 10
        if tens != 1:
            chinese_str += chinese_numbers[tens]
        chinese_str += "十"
        if ones != 0:
            chinese_str += chinese_numbers[ones]
    else:
        chinese_str += chinese_numbers[n]
    chinese_str += "课"
    return chinese_str


def build_course_title(filename: str) -> str:
    """从文件名生成课程标题"""
    name = Path(filename).stem
    # 处理小数点文件名，如 10.5 → 第10.5课
    try:
        if "." in name:
            return f"第{name}课"
        return convert_to_chinese_number(name)
    except (ValueError, IndexError):
        return name  # fallback


async def create_course_pack(
    title: str,
    description: str,
    difficulty: str = "beginner",
) -> str:
    """创建课程包，返回 ID"""
    async with async_session() as session:
        # 检查是否已存在
        result = await session.execute(
            select(CoursePack).where(CoursePack.title == title)
        )
        existing = result.scalar_one_or_none()
        if existing:
            print(f"  ⏭ 课程包已存在：{title}")
            # 删除已有的 courses + statements，重新导入
            from sqlalchemy import delete as sa_delete
            for course in await session.execute(
                select(Course).where(Course.course_pack_id == existing.id)
            ):
                pass  # cascade 会自动删除 statements
            await session.execute(
                sa_delete(Statement).where(
                    Statement.course_id.in_(
                        select(Course.id).where(Course.course_pack_id == existing.id)
                    )
                )
            )
            await session.execute(
                sa_delete(Course).where(Course.course_pack_id == existing.id)
            )
            await session.commit()
            pack_id = existing.id
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
        return pack_id


async def import_courses(
    pack_id: str,
    json_dir: Path,
) -> int:
    """导入一个目录下所有 JSON 课程文件，返回导入的 statement 总数"""
    json_files = sorted(
        [f for f in os.listdir(json_dir) if f.endswith(".json")],
        key=lambda x: float(Path(x).stem) if "." in Path(x).stem else int(Path(x).stem),
    )

    total_statements = 0

    async with async_session() as session:
        for idx, filename in enumerate(json_files):
            filepath = json_dir / filename
            course_title = build_course_title(filename)

            # 读取 JSON
            with open(filepath, "r", encoding="utf-8") as f:
                statements_data = json.load(f)

            # 创建课程
            course_id = str(uuid.uuid4())
            course = Course(
                id=course_id,
                title=course_title,
                description=None,
                order=idx + 1,
                difficulty="beginner",
                course_pack_id=pack_id,
            )
            session.add(course)
            await session.flush()  # 获取 course_id 但未提交

            # 批量创建句子
            for order_idx, stmt_data in enumerate(statements_data):
                grammar = stmt_data.get("grammar")
                # 只传有值的 grammar，避免 asyncpg 把 None 转成 JSON null
                stmt_kwargs = {
                    "id": str(uuid.uuid4()),
                    "order": order_idx + 1,
                    "chinese": stmt_data["chinese"],
                    "english": stmt_data["english"],
                    "soundmark": stmt_data.get("soundmark"),
                    "course_id": course_id,
                }
                if grammar:
                    stmt_kwargs["grammar"] = grammar
                statement = Statement(**stmt_kwargs)
                session.add(statement)
                total_statements += 1

            print(f"  ✓ {course_title}：{len(statements_data)} 个句子")

        await session.commit()

    return total_statements


async def main():
    print("=" * 60)
    print("LinguaPulse 种子数据导入")
    print("=" * 60)
    print()

    # ── 课程包 1：星荣零基础学英语 ──
    print("📦 课程包 1：星荣零基础学英语")
    pack1_id = await create_course_pack(
        title="星荣零基础学英语",
        description="最适合零基础入门的英语课程，从单词到句子循序渐进。",
        difficulty="beginner",
    )
    count1 = await import_courses(pack1_id, COURSES_DIR)
    print(f"  ✅ 共导入 {count1} 个句子\n")

    # ── 课程包 2：新概念英语第一册 ──
    print("📦 课程包 2：新概念英语第一册")
    pack2_id = await create_course_pack(
        title="新概念英语第一册",
        description="新概念英语第一册经典教材，涵盖基础语法与日常对话。",
        difficulty="intermediate",
    )
    count2 = await import_courses(pack2_id, NCE_DIR)
    print(f"  ✅ 共导入 {count2} 个句子\n")

    print("=" * 60)
    print(f"🎉 全部完成！共导入 {count1 + count2} 个句子")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
