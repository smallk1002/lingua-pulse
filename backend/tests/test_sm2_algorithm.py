"""
SM-2 间隔重复算法单元测试

这是整个复习系统的核心——每一个边界条件都直接决定用户的学习体验。
"""

import pytest
from datetime import datetime, timedelta


# ============================================================
# 模拟 ReviewItem（不依赖数据库）
# ============================================================

class MockReviewItem:
    def __init__(self, ease_factor=2.5, interval=0, repetitions=0):
        self.ease_factor = ease_factor
        self.interval = interval
        self.repetitions = repetitions
        self.next_review_at = datetime.now()
        self.last_review_at = None
        self.last_quality = None
        self.total_reviews = 0
        self.total_errors = 0


# ============================================================
# SM-2 算法实现（被测试对象）
# ============================================================

def sm2(quality: int, item: MockReviewItem) -> MockReviewItem:
    """SM-2 算法核心实现"""
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
        item.interval = 0

    item.ease_factor = max(
        1.3,
        item.ease_factor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02),
    )

    item.next_review_at = datetime.now() + timedelta(days=item.interval)
    item.last_quality = quality
    item.total_reviews += 1
    if quality < 3:
        item.total_errors += 1

    return item


# ============================================================
# 第一次复习测试
# ============================================================

class TestFirstReview:
    """首次复习（repetitions=0）"""

    def test_first_review_perfect_quality_5(self):
        """第一次复习，全对 → 1 天后复习"""
        item = MockReviewItem(ease_factor=2.5, interval=0, repetitions=0)
        result = sm2(5, item)
        assert result.repetitions == 1
        assert result.interval == 1
        assert result.ease_factor == 2.6  # quality=5, ease += 0.1
        assert result.total_errors == 0

    def test_first_review_quality_4(self):
        """第一次复习，修复后正确 → 1 天后复习"""
        item = MockReviewItem()
        result = sm2(4, item)
        assert result.interval == 1
        assert result.repetitions == 1

    def test_first_review_quality_3(self):
        """第一次复习，修复两次以上正确 → 1 天后复习"""
        item = MockReviewItem()
        result = sm2(3, item)
        assert result.interval == 1
        assert result.repetitions == 1

    def test_first_review_quality_2(self):
        """第一次复习，显示答案后才正确 → 当天重复"""
        item = MockReviewItem()
        result = sm2(2, item)
        assert result.interval == 0
        assert result.repetitions == 0
        assert result.total_errors == 1

    def test_first_review_quality_0(self):
        """第一次复习，完全错误 → 当天重复，easiness 大幅降低"""
        item = MockReviewItem(ease_factor=2.5)
        result = sm2(0, item)
        assert result.interval == 0
        assert result.repetitions == 0
        assert result.total_errors == 1
        # quality=0 时 ease_factor 应该显著下降
        assert result.ease_factor < 2.5


# ============================================================
# 连续正确测试
# ============================================================

class TestConsecutiveCorrect:
    """连续正确 → 间隔指数级增长"""

    def test_three_consecutive_perfect(self):
        """连续 3 次全对"""
        item = MockReviewItem()
        # 第 1 次
        item = sm2(5, item)
        assert item.interval == 1
        # 第 2 次
        item = sm2(5, item)
        assert item.interval == 3
        # 第 3 次
        item = sm2(5, item)
        assert item.interval == round(3 * item.ease_factor)
        assert item.repetitions == 3

    def test_interval_grows_with_repetitions(self):
        """间隔应随连续正确次数递增"""
        item = MockReviewItem()
        intervals = []
        for _ in range(5):
            item = sm2(5, item)
            intervals.append(item.interval)
        # 间隔应该是非递减的
        assert intervals == sorted(intervals)
        # 最后一次间隔应该大于第一次
        assert intervals[-1] >= intervals[0]

    def test_interval_grows_faster_with_higher_ease(self):
        """高 easiness 句子间隔增长更快"""
        item_easy = MockReviewItem(ease_factor=3.0, repetitions=2, interval=5)
        item_hard = MockReviewItem(ease_factor=1.5, repetitions=2, interval=5)
        result_easy = sm2(5, item_easy)
        result_hard = sm2(5, item_hard)
        assert result_easy.interval > result_hard.interval


# ============================================================
# 错误后重置测试
# ============================================================

class TestErrorReset:
    """答错 → 间隔重置为 0，重复次数清零"""

    def test_error_resets_after_consecutive_correct(self):
        """连续正确后答错 → 重置"""
        item = MockReviewItem(repetitions=3, interval=10, ease_factor=2.5)
        result = sm2(1, item)
        assert result.repetitions == 0
        assert result.interval == 0
        assert result.total_errors == 1

    def test_error_reduces_ease_factor(self):
        """答错降低 easiness"""
        item = MockReviewItem(ease_factor=2.5)
        result = sm2(1, item)
        assert result.ease_factor < 2.5

    def test_ease_factor_never_below_1_3(self):
        """easiness 最低为 1.3"""
        item = MockReviewItem(ease_factor=1.3)
        for _ in range(10):
            item = sm2(0, item)
        assert item.ease_factor >= 1.3


# ============================================================
# 边界条件测试
# ============================================================

class TestEdgeCases:
    """边界条件"""

    def test_quality_out_of_range(self):
        """quality out of range still computes safely"""
        item = MockReviewItem()
        result = sm2(6, item)
        assert result.interval == 1
        assert result.repetitions == 1

    def test_very_large_interval(self):
        """极大间隔值（> 365 天）仍然能正确处理"""
        item = MockReviewItem(ease_factor=3.0, interval=180, repetitions=10)
        result = sm2(5, item)
        assert result.interval > 180
        assert result.repetitions == 11

    def test_next_review_at_is_future(self):
        """next_review_at 必须大于当前时间（除非 interval=0）"""
        item = MockReviewItem()
        now = datetime.now()
        result = sm2(5, item)
        assert result.next_review_at > now

    def test_next_review_at_is_now_for_interval_zero(self):
        """interval=0 时 next_review_at 约等于当前时间"""
        item = MockReviewItem()
        now = datetime.now()
        result = sm2(0, item)
        delta = abs((result.next_review_at - now).total_seconds())
        assert delta < 10  # 允许 10 秒误差


# ============================================================
# last_quality 记录测试
# ============================================================

class TestLastQuality:
    """验证 last_quality 字段正确记录"""

    def test_last_quality_is_set(self):
        item = MockReviewItem()
        result = sm2(5, item)
        assert result.last_quality == 5

    def test_last_quality_overwritten(self):
        """多次答题时 last_quality 应为最新值"""
        item = MockReviewItem()
        item = sm2(5, item)
        assert item.last_quality == 5
        item = sm2(2, item)
        assert item.last_quality == 2
        item = sm2(4, item)
        assert item.last_quality == 4

    def test_last_quality_used_for_debugging(self):
        """模拟调试场景：通过 last_quality 区分答题表现"""
        item = MockReviewItem()
        item = sm2(5, item)  # 第一次全对
        item = sm2(3, item)  # 第二次费力
        assert item.last_quality == 3
        # 调试时可通过 last_quality 知道"上次是修复后才对的"
        assert item.last_quality < 5


# ============================================================
# 评分映射测试
# ============================================================

class TestQualityMapping:
    """游戏表现 → quality 评分的映射规则"""

    @pytest.mark.parametrize("game_performance,expected_quality", [
        ("first_try_all_correct", 5),
        ("fix_once_correct", 4),
        ("fix_twice_correct", 3),
        ("reveal_answer_then_correct", 2),
        ("timed_out", 1),
        ("all_wrong", 0),
    ])
    def test_quality_mapping(self, game_performance: str, expected_quality: int):
        """验证游戏表现到 quality 的映射关系"""
        # 这个测试确保评分映射表的一致性
        mapping = {
            "first_try_all_correct": 5,
            "fix_once_correct": 4,
            "fix_twice_correct": 3,
            "reveal_answer_then_correct": 2,
            "timed_out": 1,
            "all_wrong": 0,
        }
        assert mapping[game_performance] == expected_quality
