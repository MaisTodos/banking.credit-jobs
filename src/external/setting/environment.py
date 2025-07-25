from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.external.infrastructure.logger.level import LogLevel

path = Path(__file__).resolve()
env_file_path = Path(path.parents[3]) / ".env"


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")

    ENV: str

    APP_NAME: str
    APP_VERSION: str
    APP_HOST: str
    APP_PORT: int

    ALLOW_ORIGINS: str
    ALLOW_HEADERS: str
    ALLOW_METHODS: str

    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    AWS_LOCAL_URL: str | None = None

    DATABASE_WRITE_HOST: str
    DATABASE_WRITE_PORT: str
    DATABASE_WRITE_USER: str
    DATABASE_WRITE_PASSWORD: str
    DATABASE_WRITE_NAME: str

    DATABASE_READ_HOST: str
    DATABASE_READ_PORT: str
    DATABASE_READ_USER: str
    DATABASE_READ_PASSWORD: str
    DATABASE_READ_NAME: str

    SENTRY_DSN: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    LOG_LEVEL: LogLevel

    @field_validator("LOG_LEVEL", mode="before")
    @classmethod
    def parse_log_level(cls, value: str | int | LogLevel) -> LogLevel:
        if isinstance(value, LogLevel):
            return value
        if isinstance(value, str) and value in [level.name for level in LogLevel]:
            return LogLevel[value.upper()]

        if isinstance(value, int):
            return LogLevel(value)

        raise ValueError(f"Invalid log level: {value}")  # noqa: TRY003, EM102


env = Environment(_env_file=env_file_path)
