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

    AWS_S3_BUCKET_NAME: str
    AWS_S3_BUCKET_PATH: str
    AWS_LOCAL_URL: str | None = None

    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str

    SENTRY_DSN: str

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
