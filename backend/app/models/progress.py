"""
学习进度模型

记录用户在每个课程中的学习进度和完成历史。
"""

import uuid
from datetime import datetime

from sqlalchemy import String, Integer, DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CourseProgress(Base):
    """
    用户课程进度

    记录用户当前做到第几题（statement_index）。
    一个用户在一个课程中只有一条记录。
    """
    __tablename__ = "course_progress"
    __table_args__ = (
        UniqueConstraint("user_id", "course_id", name="uq_user_course_progress"),
    )

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    course_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False
    )
    statement_index: Mapped[int] = mapped_column(Integer, default=0)
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # 关系
    user: Mapped["User"] = relationship("User", back_populates="progress")
    course: Mapped["Course"] = relationship("Course", back_populates="progress")


class CourseHistory(Base):
    """
    课程完成历史

    记录用户每次完成课程的记录（可多次完成同一门课）。
    completion_count 累计完成次数。
    """
    __tablename__ = "course_history"
    __table_args__ = (
        UniqueConstraint(
            "user_id", "course_id", "course_pack_id",
            name="uq_user_course_history"
        ),
    )

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    course_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False
    )
    course_pack_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("course_packs.id", ondelete="CASCADE"),
        nullable=False,
    )
    completion_count: Mapped[int] = mapped_column(Integer, default=1)
    last_completed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # 关系
    course: Mapped["Course"] = relationship("Course", back_populates="history")
