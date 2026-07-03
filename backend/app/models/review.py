"""
间隔重复模型

SM-2 算法的核心数据 —— 每个句子在每个用户那里有一条 ReviewItem。
控制句子何时需要再次复习。
"""

import uuid
from datetime import datetime

from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ReviewItem(Base):
    """
    间隔重复记录

    一对一关联：一个用户 + 一个句子 = 一条 ReviewItem。
    通过 SM-2 算法动态调整下次复习时间。
    """
    __tablename__ = "review_items"
    __table_args__ = (
        UniqueConstraint("user_id", "statement_id", name="uq_user_statement_review"),
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

    # ── SM-2 核心参数 ──
    ease_factor: Mapped[float] = mapped_column(
        Float, default=2.5, nullable=False
    )  # 容易度因子，范围 [1.3, ∞)
    interval: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False
    )  # 当前间隔（天）
    repetitions: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False
    )  # 连续正确次数

    # ── 调度 ──
    next_review_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )  # 下次复习时间
    last_review_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )  # 上次复习时间

    # ── 调试字段 ──
    last_quality: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )  # 上次答题 quality 评分 (0-5)，用于算法调参

    # ── 统计 ──
    total_reviews: Mapped[int] = mapped_column(
        Integer, default=0
    )  # 总复习次数
    total_errors: Mapped[int] = mapped_column(
        Integer, default=0
    )  # 总错误次数
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # 关系
    user: Mapped["User"] = relationship("User", back_populates="review_items")
    statement: Mapped["Statement"] = relationship(
        "Statement", back_populates="review_items"
    )
