"""
所有模型导入 —— Alembic autogenerate 需要从这里 import Base 和全部模型。
"""

from app.core.database import Base

# 这些 import 必须在 Base 之后，按依赖顺序
from app.models.user import User
from app.models.course import CoursePack, Course, Statement
from app.models.progress import CourseProgress, CourseHistory
from app.models.review import ReviewItem
from app.models.others import MasteredElement, UserSettings, UserStats, LearningSession
from app.models.verification import VerificationCode, LoginAttempt

__all__ = [
    "Base",
    "User",
    "CoursePack",
    "Course",
    "Statement",
    "CourseProgress",
    "CourseHistory",
    "ReviewItem",
    "MasteredElement",
    "UserSettings",
    "UserStats",
    "LearningSession",
    "VerificationCode",
    "LoginAttempt",
]
