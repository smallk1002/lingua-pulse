"""
已掌握元素 & 用户设置 & 学习统计模型
"""

import uuid
from datetime import date, datetime

from sqlalchemy import (
    String, Integer, Float, Boolean, Date, DateTime,
    ForeignKey, UniqueConstraint, func,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class MasteredElement(Base):
    """
    已掌握句子

    用户手动标记为"已掌握"的句子，在游戏中自动跳过。
    """
    __tablename__ = "mastered_elements"
    __table_args__ = (
        UniqueConstraint("user_id", "statement_id", name="uq_user_statement_mastered"),
    )

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    statement_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("statements.id", ondelete="CASCADE"),
        nullable=False,
    )
    mastered_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # 关系
    user: Mapped["User"] = relationship("User", back_populates="mastered_elements")
    statement: Mapped["Statement"] = relationship(
        "Statement", back_populates="mastered_by"
    )


class UserSettings(Base):
    """
    用户偏好设置

    一对一：一个用户只有一条设置记录。
    分为 5 组：游戏偏好、快捷键、发音、界面、学习目标。
    """
    __tablename__ = "user_settings"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"),
        unique=True, nullable=False,
    )

    # ── 游戏偏好 ──
    game_mode: Mapped[str] = mapped_column(
        String(30), default="chinese_to_english"
    )  # chinese_to_english | dictation
    auto_next: Mapped[bool] = mapped_column(Boolean, default=False)
    space_submit: Mapped[bool] = mapped_column(Boolean, default=True)

    # ── 快捷键 (JSON) ──
    shortcut_keys: Mapped[dict] = mapped_column(
        JSONB, default=lambda: {
            "showAnswer": "ctrl+h",
            "playSound": "ctrl+j",
            "markMastered": "ctrl+m",
            "pause": "escape",
        }
    )

    # ── 发音设置 ──
    tts_voice: Mapped[str] = mapped_column(
        String(50), default="default"
    )  # default | female | british | british_f
    tts_speed: Mapped[float] = mapped_column(Float, default=1.0)  # 0.5 ~ 2.0
    tts_play_count: Mapped[int] = mapped_column(Integer, default=2)  # 1 ~ 4
    tts_interval: Mapped[int] = mapped_column(Integer, default=3)  # 1 ~ 10 秒

    # ── 界面 ──
    theme: Mapped[str] = mapped_column(String(10), default="dark")  # dark | light
    font_size: Mapped[str] = mapped_column(
        String(10), default="medium"
    )  # small | medium | large

    # ── 学习目标 ──
    daily_goal: Mapped[int] = mapped_column(Integer, default=20)  # 每日目标题目数

    # 关系
    user: Mapped["User"] = relationship("User", back_populates="settings")


class UserStats(Base):
    """
    用户游戏化数据

    一对一：一个用户只有一条统计记录。
    包含 XP、等级、连胜等游戏化指标。
    """
    __tablename__ = "user_stats"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"),
        unique=True, nullable=False,
    )

    xp: Mapped[int] = mapped_column(Integer, default=0)
    level: Mapped[int] = mapped_column(Integer, default=1)
    streak: Mapped[int] = mapped_column(Integer, default=0)
    longest_streak: Mapped[int] = mapped_column(Integer, default=0)
    last_study_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    total_statements: Mapped[int] = mapped_column(Integer, default=0)
    total_duration: Mapped[int] = mapped_column(Integer, default=0)  # 秒
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # 关系
    user: Mapped["User"] = relationship("User", back_populates="stats")


class LearningSession(Base):
    """
    每日学习记录

    按用户 + 日期聚合，记录每天的学习时长和完成句子数。
    每 30 秒前端上报一次。
    """
    __tablename__ = "learning_sessions"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    date: Mapped[date] = mapped_column(Date, server_default=func.current_date())
    duration: Mapped[int] = mapped_column(Integer, default=0)  # 秒
    statements_count: Mapped[int] = mapped_column(Integer, default=0)
    course_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # 关系
    user: Mapped["User"] = relationship("User", back_populates="learning_sessions")

    __table_args__ = (
        {"info": {"description": "按 user_id + date 创建联合索引，加速每日统计查询"}},
    )
