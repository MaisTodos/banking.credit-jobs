from enum import Enum


class LogLevel(Enum):
    CRITICAL = 50
    FATAL = 50  # noqa: PIE796
    ERROR = 40
    WARNING = 30
    WARN = 30  # noqa: PIE796
    INFO = 20
    DEBUG = 10
    NOTSET = 0
