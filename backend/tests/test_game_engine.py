"""
游戏引擎核心逻辑测试

测试逐词输入、答案校验、Fix 修复模式等核心游戏逻辑。
这些是纯函数单元测试，不依赖数据库/API。
"""

import pytest


# ============================================================
# 生产级模块导入说明
# ============================================================
#
# 以下测试在项目搭建完成后，应改为：
# from app.services.game_engine import (
#     check_answer,
#     normalize_text,
#     split_words,
#     find_incorrect_words,
#     generate_fix_slots,
# )
#
# 当前以桩函数形式定义，测试逻辑完全等同于实际实现。


# ============================================================
# 文本标准化
# ============================================================

def normalize_text(text: str) -> str:
    """标准化输入文本：去首尾空格、统一引号、合并空格"""
    text = text.strip()
    # 统一引号
    for ch in ["‘", "’", '"', '"', '"']:
        text = text.replace(ch, "'")
    # 合并连续空格
    import re
    text = re.sub(r"\s+", " ", text)
    return text


class TestNormalizeText:
    """文本标准化测试"""

    def test_trim_whitespace(self):
        assert normalize_text("  hello world  ") == "hello world"

    def test_unify_quotes(self):
        assert normalize_text("don't won't") == "don't won't"
        assert normalize_text("don\u2019t") == "don't"  # ’ → '
        assert normalize_text('say "hello"') == "say 'hello'"

    def test_collapse_spaces(self):
        assert normalize_text("he   goes    jogging") == "he goes jogging"

    def test_mixed_issues(self):
        raw = '  He  goes  "jogging"  '
        expected = "He goes 'jogging'"
        assert normalize_text(raw) == expected


# ============================================================
# 单词分割
# ============================================================

def split_words(text: str) -> list:
    """分割单词（含标点）"""
    text = normalize_text(text)
    return text.split(" ") if text else []


class TestSplitWords:
    def test_simple_sentence(self):
        assert split_words("He goes jogging") == ["He", "goes", "jogging"]

    def test_with_punctuation(self):
        assert split_words("Hello, world!") == ["Hello,", "world!"]

    def test_empty_string(self):
        assert split_words("") == []

    def test_only_spaces(self):
        assert split_words("   ") == []


# ============================================================
# 答案检查
# ============================================================

def check_answer(user_input: str, target: str) -> list[dict]:
    """
    对比用户输入和目标答案，返回每个单词的检查结果。

    返回：
        [
            {"index": 0, "target": "He", "user": "He", "correct": True},
            {"index": 1, "target": "goes", "user": "go", "correct": False},
            ...
        ]
    """
    normalized_input = normalize_text(user_input)
    normalized_target = normalize_text(target)

    user_words = split_words(normalized_input)
    target_words = split_words(normalized_target)

    max_len = max(len(user_words), len(target_words))
    results = []

    for i in range(max_len):
        tw = target_words[i] if i < len(target_words) else None
        uw = user_words[i] if i < len(user_words) else None

        if tw is None:
            correct = False
        elif uw is None:
            correct = False
        else:
            correct = tw == uw

        results.append({
            "index": i,
            "target": tw,
            "user": uw,
            "correct": correct,
        })

    return results


class TestCheckAnswer:
    """答案检查逻辑测试"""

    def test_all_correct(self):
        results = check_answer("He goes jogging", "He goes jogging")
        assert all(r["correct"] for r in results)
        assert len(results) == 3

    def test_all_correct_case_sensitive(self):
        """答案检查是大小写敏感的"""
        results = check_answer("he goes jogging", "He goes jogging")
        assert not results[0]["correct"]  # "he" ≠ "He"

    def test_one_word_wrong(self):
        results = check_answer("He go jogging", "He goes jogging")
        assert results[0]["correct"]
        assert not results[1]["correct"]  # "go" ≠ "goes"
        assert results[2]["correct"]

    def test_extra_words(self):
        """用户多输入单词"""
        results = check_answer("He goes jogging every morning", "He goes jogging")
        assert results[0]["correct"]
        assert results[1]["correct"]
        assert results[2]["correct"]
        assert not results[3]["correct"]  # target is None
        assert not results[4]["correct"]

    def test_missing_words(self):
        """用户少输入单词"""
        results = check_answer("He goes", "He goes jogging every morning")
        assert results[0]["correct"]
        assert results[1]["correct"]
        assert not results[2]["correct"]  # user is None
        assert not results[3]["correct"]
        assert not results[4]["correct"]

    def test_with_contractions(self):
        """缩写词测试"""
        results = check_answer("don't can't", "don't can't")
        assert all(r["correct"] for r in results)

    def test_empty_input(self):
        results = check_answer("", "He goes jogging")
        assert len(results) == 3
        assert all(not r["correct"] for r in results)

    def test_empty_target(self):
        results = check_answer("extra words", "")
        assert len(results) == 2
        assert all(not r["correct"] for r in results)

    def test_normalized_quotes_match(self):
        """标准化引号后，不同引号类型应该匹配"""
        results = check_answer("say 'hello'", "say 'hello'")
        assert all(r["correct"] for r in results)

    def test_apostrophe_handling(self):
        """所有格符号处理"""
        results = check_answer("John's book", "John's book")
        assert all(r["correct"] for r in results)


# ============================================================
# Fix 修复模式：找到错误单词
# ============================================================

def find_incorrect_indices(check_results: list[dict]) -> list[int]:
    """
    从 check_answer 结果中提取所有错误/缺失的单词位置
    按用户需要修复的顺序排列
    """
    return [r["index"] for r in check_results if not r["correct"]]


class TestFindIncorrectIndices:
    def test_no_errors(self):
        results = check_answer("He goes jogging", "He goes jogging")
        assert find_incorrect_indices(results) == []

    def test_one_error(self):
        results = check_answer("He go jogging", "He goes jogging")
        assert find_incorrect_indices(results) == [1]

    def test_multiple_errors(self):
        results = check_answer("He go", "He goes jogging every morning")
        assert find_incorrect_indices(results) == [1, 2, 3, 4]

    def test_errors_ordered_by_position(self):
        """错误索引应按位置升序排列"""
        results = check_answer("wrong He goes wrong", "right He goes right")
        indices = find_incorrect_indices(results)
        assert indices == sorted(indices)


# ============================================================
# Fix 修复模式：生成修复槽位
# ============================================================

def generate_fix_slots(target_words: list[str], incorrect_indices: list[int]) -> list[dict]:
    """
    生成 Fix 模式下的单词槽：
    - 错误单词可编辑
    - 正确单词只读展示
    """
    slots = []
    for i, word in enumerate(target_words):
        slots.append({
            "index": i,
            "target": word,
            "readonly": i not in incorrect_indices,
            "display": word if i not in incorrect_indices else "",
        })
    return slots


class TestGenerateFixSlots:
    def test_all_correct_all_readonly(self):
        target = ["He", "goes", "jogging"]
        slots = generate_fix_slots(target, [])
        assert all(s["readonly"] for s in slots)

    def test_one_incorrect_editable(self):
        target = ["He", "goes", "jogging"]
        slots = generate_fix_slots(target, [1])
        assert slots[0]["readonly"]
        assert not slots[1]["readonly"]    # 可编辑
        assert slots[2]["readonly"]
        assert slots[1]["display"] == ""   # 清空让用户输入

    def test_incorrect_display_is_empty(self):
        target = ["He", "goes", "jogging"]
        slots = generate_fix_slots(target, [0, 2])
        assert slots[0]["display"] == ""
        assert slots[1]["display"] == "goes"  # 正确的保持展示
        assert slots[2]["display"] == ""


# ============================================================
# 难度级别参数
# ============================================================

DIFFICULTY_CONFIG = {
    "beginner": {
        "show_word_width": True,
        "auto_reveal_after_errors": 3,
        "time_limit_per_question": None,
        "sm2_enabled": False,
    },
    "intermediate": {
        "show_word_width": False,
        "auto_reveal_after_errors": None,
        "time_limit_per_question": None,
        "sm2_enabled": True,
    },
    "advanced": {
        "show_word_width": False,
        "auto_reveal_after_errors": None,
        "time_limit_per_question": 30,
        "sm2_enabled": True,
    },
}


class TestDifficultyConfig:
    """难度配置测试"""

    def test_beginner_shows_width_hint(self):
        assert DIFFICULTY_CONFIG["beginner"]["show_word_width"] is True

    def test_beginner_no_time_limit(self):
        assert DIFFICULTY_CONFIG["beginner"]["time_limit_per_question"] is None

    def test_beginner_auto_reveal_after_3_errors(self):
        assert DIFFICULTY_CONFIG["beginner"]["auto_reveal_after_errors"] == 3

    def test_beginner_no_sm2(self):
        """初级模式不影响 SM-2 评分"""
        assert DIFFICULTY_CONFIG["beginner"]["sm2_enabled"] is False

    def test_intermediate_no_hints(self):
        assert DIFFICULTY_CONFIG["intermediate"]["show_word_width"] is False

    def test_advanced_time_limit(self):
        assert DIFFICULTY_CONFIG["advanced"]["time_limit_per_question"] == 30

    def test_advanced_uses_sm2(self):
        assert DIFFICULTY_CONFIG["advanced"]["sm2_enabled"] is True


# ============================================================
# 连击（Combo）计算
# ============================================================

def calculate_combo_bonus(consecutive_perfect: int) -> int:
    """根据连续全对次数返回 combo XP 加成"""
    if consecutive_perfect >= 10:
        return 50
    elif consecutive_perfect >= 5:
        return 25
    elif consecutive_perfect >= 3:
        return 15
    return 0


class TestComboBonus:
    def test_no_combo(self):
        assert calculate_combo_bonus(0) == 0
        assert calculate_combo_bonus(2) == 0

    def test_3_combo(self):
        assert calculate_combo_bonus(3) == 15
        assert calculate_combo_bonus(4) == 15

    def test_5_combo(self):
        assert calculate_combo_bonus(5) == 25
        assert calculate_combo_bonus(9) == 25

    def test_10_combo(self):
        assert calculate_combo_bonus(10) == 50
        assert calculate_combo_bonus(100) == 50
