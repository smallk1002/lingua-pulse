"""
将真实 CET-4 词表转换为 Earthworm 课程格式。

数据来源：KyleBing/english-vocabulary (GitHub)
- 原始数据：json_original/json-sentence/CET4_1/2/3.json
- 基于教育部大学英语四级考试大纲，共 4544 个唯一单词
- 包含：英美音标、多词性释义、例句、短语搭配

输出：app/data/earthworm/cet4/01.json ~ 30.json
每课约 151 个单词，共 30 课。

用法：
  uv run python convert_real_cet4.py
"""

import json
import sys
from pathlib import Path

# ── 配置 ──

SOURCE_DIR = Path(__file__).parent / "_tmp_cet4_full"
SOURCE_FILE = SOURCE_DIR / "CET4_all.json"
OUTPUT_DIR = Path(__file__).parent / "app" / "data" / "earthworm" / "cet4"
LESSON_COUNT = 30


def load_and_deduplicate() -> list[dict]:
    """
    加载 KyleBing CET-4 数据，按 word 去重（保留首次出现）。
    返回标准化单词列表。
    """
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    seen = set()
    words = []

    for item in raw:
        w = item.get("word", "").strip()
        if not w or len(w) > 40:
            continue
        low = w.lower()
        if low in seen:
            continue
        seen.add(low)

        # 解析翻译和词性
        trans_list = item.get("translations", [])
        if not trans_list:
            continue

        chinese_parts = []
        pos_set = set()
        for t in trans_list:
            cn = t.get("translation", "").strip()
            pos = t.get("type", "").strip()
            if cn:
                chinese_parts.append(cn)
            if pos:
                pos_set.add(pos)

        if not chinese_parts:
            continue

        chinese = "；".join(chinese_parts)
        pos_label = "，".join(pos_set) if pos_set else ""

        # 音标：优先美音
        soundmark = ""
        us = item.get("us", "").strip()
        uk = item.get("uk", "").strip()
        if us:
            soundmark = us
        elif uk:
            soundmark = uk
        # 确保有斜杠
        if soundmark and not soundmark.startswith("/"):
            soundmark = f"/{soundmark}/"

        # 例句：取第一个
        sentences = item.get("sentences", [])
        example_en = ""
        example_cn = ""
        if sentences:
            s = sentences[0]
            example_en = s.get("sentence", "").strip()
            example_cn = s.get("translation", "").strip()

        # 短语：取前 3 个
        phrases = item.get("phrases", [])
        phrase_texts = []
        for p in phrases[:3]:
            p_text = p.get("phrase", "").strip()
            p_cn = p.get("translation", "").strip()
            if p_text:
                phrase_texts.append(f"{p_text} ({p_cn})" if p_cn else p_text)

        words.append({
            "word": w,
            "chinese": chinese,
            "soundmark": soundmark,
            "pos": pos_label,
            "example_en": example_en,
            "example_cn": example_cn,
            "phrases": phrase_texts,
        })

    return words


def generate_lessons(words: list[dict]) -> list[list[dict]]:
    """将单词列表均分为 30 课"""
    total = len(words)
    per_lesson = total // LESSON_COUNT
    remainder = total % LESSON_COUNT

    lessons = []
    idx = 0
    for lesson_no in range(LESSON_COUNT):
        count = per_lesson + (1 if lesson_no < remainder else 0)
        lesson_words = words[idx:idx + count]
        idx += count

        statements = []
        for w in lesson_words:
            grammar = None
            if w["pos"]:
                grammar = [{"label": w["pos"], "text": f"{w['pos']}：{w['chinese']}"}]

            statements.append({
                "chinese": w["chinese"],
                "english": w["word"],
                "soundmark": w["soundmark"],
                "grammar": grammar,
            })

        lessons.append(statements)

    return lessons


def main():
    print("=" * 60)
    print("🔄 真实 CET-4 数据转换 (KyleBing 4544词 → Earthworm)")
    print("=" * 60)
    print()

    if not SOURCE_FILE.exists():
        print(f"❌ 源文件不存在: {SOURCE_FILE}")
        print("   请先下载 KyleBing CET-4 数据到 _tmp_cet4_full/")
        sys.exit(1)

    # 1. 加载并去重
    print("📖 加载并去重 ...")
    words = load_and_deduplicate()
    print(f"   ✅ 去重后: {len(words)} 个唯一单词")
    print()

    # 2. 统计
    with_soundmark = sum(1 for w in words if w["soundmark"])
    with_example = sum(1 for w in words if w["example_en"])
    with_phrase = sum(1 for w in words if w["phrases"])
    with_pos = sum(1 for w in words if w["pos"])
    print("📊 数据统计：")
    print(f"   总单词数:    {len(words)}")
    print(f"   有音标:      {with_soundmark} ({with_soundmark * 100 // len(words)}%)")
    print(f"   有词性标注:  {with_pos} ({with_pos * 100 // len(words)}%)")
    print(f"   有例句:      {with_example} ({with_example * 100 // len(words)}%)")
    print(f"   有短语:      {with_phrase} ({with_phrase * 100 // len(words)}%)")
    print()

    # 样例
    print("📋 样例（前 5 个单词）：")
    for w in words[:5]:
        pos = f"[{w['pos']}] " if w['pos'] else ""
        print(f"   {w['word']:18s} {pos}{w['chinese'][:40]}")
        if w['soundmark']:
            print(f"   {'':18s} 音标: {w['soundmark']}")
        if w['phrases']:
            print(f"   {'':18s} 短语: {'; '.join(w['phrases'][:2])}")
        if w['example_en']:
            print(f"   {'':18s} 例句: {w['example_en']} — {w['example_cn']}")
    print()

    # 3. 分课
    print(f"📚 分课处理（{LESSON_COUNT} 课）...")
    lessons = generate_lessons(words)
    for i, lesson in enumerate(lessons):
        print(f"   第 {i+1:02d} 课: {len(lesson)} 条语句")
    print()

    # 4. 写入
    print(f"💾 写入 {OUTPUT_DIR} ...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, lesson in enumerate(lessons):
        filepath = OUTPUT_DIR / f"{i+1:02d}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(lesson, f, ensure_ascii=False, indent=2)
    print(f"   ✅ 已写入 {len(lessons)} 个文件")
    print()

    # 5. 总结
    print("=" * 60)
    print(f"✅ 转换完成！")
    print(f"   {len(words)} 个真实 CET-4 单词 → {LESSON_COUNT} 课 → {sum(len(l) for l in lessons)} 条语句")
    print()
    print("📌 下一步：运行种子数据导入")
    print("   uv run python seed_earthworm.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
