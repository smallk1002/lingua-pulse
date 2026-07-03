"""
TTS、设置、统计相关 Pydantic 模型
"""

from datetime import date, datetime
from pydantic import BaseModel, Field


# ── TTS ──

class TTSGenerateRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1000)
    voice: str = "default"
    speed: str = "+0%"


class TTSGenerateResponse(BaseModel):
    url: str


class TTSBatchRequest(BaseModel):
    statement_ids: list[str]
    voice: str = "default"


class TTSBatchItem(BaseModel):
    statement_id: str
    url: str


class TTSBatchResponse(BaseModel):
    results: list[TTSBatchItem]


# ── Settings ──

class SettingsOut(BaseModel):
    game_mode: str = "chinese_to_english"
    auto_next: bool = False
    space_submit: bool = True
    shortcut_keys: dict = {}
    tts_voice: str = "default"
    tts_speed: float = 1.0
    tts_play_count: int = 2
    tts_interval: int = 3
    theme: str = "dark"
    font_size: str = "medium"
    daily_goal: int = 20

    model_config = {"from_attributes": True}


class SettingsUpdate(BaseModel):
    game_mode: str | None = None
    auto_next: bool | None = None
    space_submit: bool | None = None
    shortcut_keys: dict | None = None
    tts_voice: str | None = None
    tts_speed: float | None = None
    tts_play_count: int | None = None
    tts_interval: int | None = None
    theme: str | None = None
    font_size: str | None = None
    daily_goal: int | None = None


# ── Stats ──

class StatsSummaryOut(BaseModel):
    xp: int = 0
    level: int = 1
    streak: int = 0
    longest_streak: int = 0
    total_statements: int = 0
    total_duration: int = 0
    xp_to_next_level: int = 0


class DailyStatsOut(BaseModel):
    date: date
    duration: int
    statements_count: int


class SessionReport(BaseModel):
    duration: int = Field(ge=0)  # 秒
    statements_count: int = Field(ge=0)
    course_id: str | None = None
