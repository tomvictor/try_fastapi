from pydantic import BaseSettings
import secrets


class Settings(BaseSettings):
    ENV: str = "DEFAULT"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)


settings = Settings()
