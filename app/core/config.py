import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = "DEFAULT"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:asd123##@localhost/app"


settings = Settings()
