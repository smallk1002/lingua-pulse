from app.api.auth import router as auth_router
from app.api.courses import router as courses_router
from app.api.game import router as game_router
from app.api.tts_settings_stats import router as tts_settings_stats_router
from app.api.admin import router as admin_router

__all__ = [
    "auth_router",
    "courses_router",
    "game_router",
    "tts_settings_stats_router",
    "admin_router",
]
