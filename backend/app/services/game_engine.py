"""
游戏引擎服务

包含：
- SM-2 间隔重复算法
- 答案标准化 & 逐词检查
- XP 计算
"""

from datetime import datetime, timedelta

from app.models.review import ReviewItem


# ── SM-2 算法 ──

def sm2_algorithm(quality: int, item: ReviewItem) -> ReviewItem:
    """
    SM-2 间隔重复算法核心实现

    Args:
        quality: 0-5 答题质量评分
        item: 当前的 ReviewItem 记录

    quality 评分映射：
      5 = 第一遍全对
      4 = Fix 一次后正确
      3 = Fix 两次以上正确
      2 = 显示答案后才正确
      1 = 高级模式超时
      0 = 完全提交失败
    """
    if quality >= 3:
        if item.repetitions == 0:
            item.interval = 1
        elif item.repetitions == 1:
            item.interval = 3
        else:
            item.interval = round(item.interval * item.ease_factor)
        item.repetitions += 1
    else:
        item.repetitions = 0
        item.interval = 0  # 当天再次复习

    # 更新容易度因子（最低 1.3）
    item.ease_factor = max(
        1.3,
        item.ease_factor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02),
    )

    item.next_review_at = datetime.utcnow() + timedelta(days=item.interval)
    item.last_quality = quality
    item.last_review_at = datetime.utcnow()
    item.total_reviews += 1
    if quality < 3:
        item.total_errors += 1

    return item


# ── 答案标准化 ──

def normalize_text(text: str) -> str:
    """
    标准化用户输入和目标文本，用于逐词比较。

    规则：
    1. 去除首尾空格
    2. 统一引号：所有变体 → 直引号 '
    3. 多个连续空格合并为一个
    """
    import re

    text = text.strip()
    # 统一各种引号变体为直引号
    text = re.sub(r"[\u2018\u2019\u201a\u201b]", "'", text)  # 左/右/低单引号
    text = re.sub(r"[\u201c\u201d\u201e\u201f]", '"', text)  # 左/右/低双引号
    # 多个空格合并
    text = re.sub(r"\s+", " ", text)
    return text


# ── 逐词检查 ──

def check_answer(user_input: str, target: str) -> dict:
    """
    逐词对比用户输入与目标答案。

    Returns:
        {
            "correct": bool,
            "incorrect_words": list[int],   # 错误单词的索引
            "total_words": int,
        }
    """
    user_norm = normalize_text(user_input)
    target_norm = normalize_text(target)

    user_words = user_norm.split()
    target_words = target_norm.split()

    incorrect_words = []
    max_len = max(len(user_words), len(target_words))

    for i in range(max_len):
        u_word = user_words[i] if i < len(user_words) else ""
        t_word = target_words[i] if i < len(target_words) else ""
        if u_word != t_word:
            incorrect_words.append(i)

    correct = len(incorrect_words) == 0 and len(user_words) == len(target_words)
    return {
        "correct": correct,
        "incorrect_words": incorrect_words,
        "total_words": len(target_words),
    }


# ── Quality 计算 ──

def calc_quality(fix_count: int, difficulty: str, is_timeout: bool = False) -> int:
    """
    根据用户表现计算 SM-2 quality 评分。

    Args:
        fix_count: 进入 Fix 修复模式的次数
        difficulty: beginner | intermediate | advanced
        is_timeout: 是否超时（高级模式）
    """
    if is_timeout:
        return 1

    if fix_count == 0:
        return 5
    elif fix_count == 1:
        quality = 4
    elif fix_count == 2:
        quality = 3
    else:
        quality = 2  # 多次修复才正确

    # 高级模式重罚
    if difficulty == "advanced" and fix_count > 0:
        quality = max(1, quality - 1)

    return quality


# ── XP 计算 ──

def calc_xp(
    quality: int,
    combo: int = 0,
    is_review: bool = False,
    is_first_of_day: bool = False,
) -> int:
    """
    计算本次答题获得的 XP。

    combo: 连续全对次数
    """
    base = 8 if is_review else 10

    if quality == 5:
        if combo >= 5:
            base = 25
        elif combo >= 3:
            base = 15
    elif quality >= 3:
        base = 5  # 修复后正确
    else:
        base = 2

    if is_first_of_day:
        base += 20

    return base
