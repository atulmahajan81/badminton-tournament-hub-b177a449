# backend/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    database_url: str
    cors_origins: list[str] = ["https://allowed-domain.com"]  # Change this to actual allowed domains

    class Config:
        env_file = ".env"

settings = Settings()