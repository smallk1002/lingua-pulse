"""
用户表

核心认证主体，所有学习数据关联此表。
"""

import uuid
from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )
    username: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # 关系
    settings: Mapped["UserSettings"] = relationship(
        "UserSettings", back_populates="user", uselist=False
    )
    stats: Mapped["UserStats"] = relationship(
        "UserStats", back_populates="user", uselist=False
    )
    course_packs: Mapped[list["CoursePack"]] = relationship(
        "CoursePack", back_populates="creator"
    )
    progress: Mapped[list["CourseProgress"]] = relationship(
        "CourseProgress", back_populates="user"
    )
    review_items: Mapped[list["ReviewItem"]] = relationship(
        "ReviewItem", back_populates="user"
    )
    mastered_elements: Mapped[list["MasteredElement"]] = relationship(
        "MasteredElement", back_populates="user"
    )
    learning_sessions: Mapped[list["LearningSession"]] = relationship(
        "LearningSession", back_populates="user"
    )
