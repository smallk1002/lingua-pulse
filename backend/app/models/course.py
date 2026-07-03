"""
课程体系模型

三层结构：CoursePack（课程包） → Course（课程） → Statement（句子）
"""

import uuid
from datetime import datetime

from sqlalchemy import String, Integer, Boolean, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CoursePack(Base):
    """
    课程包

    一组相关课程的集合，如「基础英语 100 句」「商务英语常用句」。
    """
    __tablename__ = "course_packs"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    cover_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    difficulty: Mapped[str] = mapped_column(
        String(20), default="beginner"
    )  # beginner | intermediate | advanced
    is_public: Mapped[bool] = mapped_column(Boolean, default=False)
    creator_id: Mapped[str | None] = mapped_column(
        UUID(as_uuid=False), ForeignKey("users.id"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # 关系
    creator: Mapped["User"] = relationship("User", back_populates="course_packs")
    courses: Mapped[list["Course"]] = relationship(
        "Course", back_populates="course_pack", order_by="Course.order"
    )


class Course(Base):
    """
    课程

    课程包下的一课，如「基础英语 100 句」下的「第 5 课：日常活动描述」。
    """
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    difficulty: Mapped[str] = mapped_column(String(20), default="intermediate")
    course_pack_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("course_packs.id", ondelete="CASCADE"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # 关系
    course_pack: Mapped["CoursePack"] = relationship(
        "CoursePack", back_populates="courses"
    )
    statements: Mapped[list["Statement"]] = relationship(
        "Statement", back_populates="course", order_by="Statement.order",
        cascade="all, delete-orphan"
    )
    progress: Mapped[list["CourseProgress"]] = relationship(
        "CourseProgress", back_populates="course"
    )
    history: Mapped[list["CourseHistory"]] = relationship(
        "CourseHistory", back_populates="course"
    )


class Statement(Base):
    """
    句子（题目）

    每个句子包含英文原句、中文翻译、音标和语法分析 JSON。
    用户练习的基本单元。
    """
    __tablename__ = "statements"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    chinese: Mapped[str] = mapped_column(Text, nullable=False)
    english: Mapped[str] = mapped_column(Text, nullable=False)
    soundmark: Mapped[str | None] = mapped_column(String(500), nullable=True)
    grammar: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    tts_audio_url: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )  # edge-tts 生成的音频 URL
    course_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # 关系
    course: Mapped["Course"] = relationship("Course", back_populates="statements")
    review_items: Mapped[list["ReviewItem"]] = relationship(
        "ReviewItem", back_populates="statement"
    )
    mastered_by: Mapped[list["MasteredElement"]] = relationship(
        "MasteredElement", back_populates="statement"
    )
