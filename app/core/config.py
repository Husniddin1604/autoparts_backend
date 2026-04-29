from pathlib import Path
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # application configuration
    DEBUG: bool  # Debug mode for the application
    APP_MODE: str
    ADMIN_USERNAME: str  # Admin username for the starlette_admin
    ADMIN_PASSWORD: str  # Admin credentials for the starlette_admin
    SECRET_KEY: str  # Secret key for the application, used for signing tokens and cookies
    CORS_ALLOWED_ORIGINS: str  # Comma-separated list of allowed origins for CORS
    ACCESS_TOKEN_EXPIRE_MINUTES: int = (
        60  # Expiration time for access tokens in minutes
    )
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30  # Expiration time for refresh tokens in days

    # Postgresql configuration
    POSTGRES_PORT: int  # PostgreSQL port for the application
    POSTGRES_HOST: str  # PostgreSQL host for the application
    POSTGRES_USER: str  # PostgreSQL user for the application
    POSTGRES_PASSWORD: str  # Password for the PostgreSQL user
    POSTGRES_DB: str  # Database name for the application

    # MinIO configuration
    MINIO_HOST: str  # MinIO host for file storage
    MINIO_PORT: int  # MinIO port for file storage
    MINIO_ACCESS_KEY: str  # MinIO access key for file storage
    MINIO_SECRET_KEY: str  # MinIO secret key for file storage

    # KAFKA_USERNAME: str  # Kafka username for authentication
    # KAFKA_PASSWORD: str  # Kafka password for authentication
    # KAFKA_BOOTSTRAP_SERVERS: str  # Kafka bootstrap servers

    # Redis configuration
    REDIS_HOST: str  # Redis host for job scheduling
    REDIS_PORT: int  # Redis port for job scheduling
    REDIS_PASSWORD: str  # Redis password for job scheduling
    REDIS_DB: int  # Redis database for job scheduling
    REDIS_URL: str  # Redis URL for caching and session management


    # Telegram bot settings
    # API_TOKEN: str
    # CHAT_ID: int

    # DATABASE_URL is a computed property that constructs the database URL
    @property
    def DATABASE_URL(self):
        password = quote_plus(self.POSTGRES_PASSWORD)
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{password}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent / ".env"),  # ✅ full path
        extra="ignore",
    )


settings = Settings()
