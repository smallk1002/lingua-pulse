"""
LinguaPulse API 服务入口

启动：uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import (
    auth_router,
    courses_router,
    game_router,
    tts_settings_stats_router,
    admin_router,
)
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url=None,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth_router)
app.include_router(courses_router)
app.include_router(game_router)
app.include_router(tts_settings_stats_router)
app.include_router(admin_router)


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "app": settings.APP_NAME}
