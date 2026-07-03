"""
应用配置管理

所有配置通过环境变量注入，Docker Compose 中设置。
本地开发可创建 .env 文件。
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 数据库
    DATABASE_URL: str = "postgresql+asyncpg://root:admin123@localhost:5432/linguapulse"

    # JWT
    JWT_SECRET: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 天

    # TTS
    AUDIO_DIR: str = "./static/audio"

    # 应用
    APP_NAME: str = "LinguaPulse API"
    DEBUG: bool = True

    model_config = {"env_prefix": ""}


settings = Settings()
