"""
课程相关 Pydantic 模型
"""

from datetime import datetime
from pydantic import BaseModel, Field


# ── Statement ──

class StatementOut(BaseModel):
    id: str
    order: int
    chinese: str
    english: str
    soundmark: str | None = None
    grammar: list | dict | None = None  # JSONB: 语法分析数组
    tts_audio_url: str | None = None
    course_id: str | None = None  # 更多例句需要知道来源课程

    model_config = {"from_attributes": True}


class StatementCreate(BaseModel):
    order: int
    chinese: str
    english: str
    soundmark: str | None = None
    grammar: list | dict | None = None  # JSONB
    course_id: str


class StatementUpdate(BaseModel):
    order: int | None = None
    chinese: str | None = None
    english: str | None = None
    soundmark: str | None = None
    grammar: list | dict | None = None  # JSONB


class StatementReorder(BaseModel):
    statement_ids: list[str]  # 按新顺序排列的 ID 列表


# ── Course ──

class CourseOut(BaseModel):
    id: str
    title: str
    description: str | None = None
    order: int
    difficulty: str
    created_at: datetime

    model_config = {"from_attributes": True}


class CourseDetailOut(CourseOut):
    statements: list[StatementOut] = []
    progress: "CourseProgressOut | None" = None


class CourseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    order: int
    difficulty: str = "beginner"
    course_pack_id: str


class CourseUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    order: int | None = None
    difficulty: str | None = None


# ── CoursePack ──

class CoursePackOut(BaseModel):
    id: str
    title: str
    description: str | None = None
    cover_url: str | None = None
    difficulty: str
    is_public: bool
    creator_id: str | None = None
    created_at: datetime
    course_count: int = 0
    statement_count: int = 0
    last_active: datetime | None = None  # 最近学习时间
    last_course_id: str | None = None   # 上次学习的课程 ID（断点续学）

    model_config = {"from_attributes": True}


class CoursePackDetailOut(CoursePackOut):
    courses: list[CourseOut] = []


class CoursePackCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    cover_url: str | None = None
    difficulty: str = "beginner"
    is_public: bool = False


class CoursePackUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    cover_url: str | None = None
    difficulty: str | None = None
    is_public: bool | None = None


# ── Progress ──

class CourseProgressOut(BaseModel):
    statement_index: int
    completed_at: datetime | None = None

    model_config = {"from_attributes": True}


class ProgressUpdate(BaseModel):
    statement_index: int
    input_snapshot: str | None = None


class CompleteCourseRequest(BaseModel):
    """完成课程请求（可附带答题结果，用于 SM-2 批量写入）"""
    results: list["ReviewItemData"] = []
    xp_earned: int = 0  # 前端计算的 XP（用于课程进度上报）


class ReviewItemData(BaseModel):
    statement_id: str
    quality: int
    interval: int = 0
    ease_factor: float = 2.5
    repetitions: int = 0
