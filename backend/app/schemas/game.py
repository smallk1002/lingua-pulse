"""
游戏 & 复习相关 Pydantic 模型
"""

from datetime import datetime
from pydantic import BaseModel, Field


class AnswerSubmit(BaseModel):
    """前端提交答题结果"""
    statement_id: str
    user_input: str  # 用户原始输入
    difficulty: str = "intermediate"  # beginner | intermediate | advanced
    fix_count: int = 0  # 进入 Fix 修复的次数（0 = 一次全对）


class AnswerResult(BaseModel):
    """答题检查结果"""
    correct: bool
    incorrect_words: list[int] = []  # 错误单词的索引列表
    normalized_input: str  # 标准化后的用户输入
    quality: int  # SM-2 quality 评分 0-5
    xp_earned: int = 0


class ReviewItemOut(BaseModel):
    id: str
    statement_id: str
    ease_factor: float
    interval: int
    repetitions: int
    next_review_at: datetime
    last_review_at: datetime | None = None
    last_quality: int | None = None
    total_reviews: int
    total_errors: int

    model_config = {"from_attributes": True}


class ReviewSubmit(BaseModel):
    """提交 SM-2 评分（答题完成后）"""
    statement_id: str
    quality: int = Field(ge=0, le=5)


class MasterToggle(BaseModel):
    mastered: bool  # true=标记掌握, false=取消掌握
