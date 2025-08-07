from src.external.infrastructure.logger.config import JsonLogger


def init_json_logger(log_level: int):
    JsonLogger(logger="adapter", level=log_level).configure_log()
    JsonLogger(logger="application", level=log_level).configure_log()
    JsonLogger(logger="domain", level=log_level).configure_log()
    JsonLogger(logger="external", level=log_level).configure_log()
