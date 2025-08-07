import logging
import sys

import json_logging

from src.external.infrastructure.logger.formatter import CreditJobsJsonFormatter


class JsonLogger:
    def __init__(
        self,
        logger: str,
        enable_json: bool = True,
        level: int = logging.DEBUG,
    ):
        self.__logger = logger
        self.__enable_json = enable_json
        self.__level = level

    def configure_log(self) -> None:
        json_logging.init_non_web(
            custom_formatter=CreditJobsJsonFormatter,
            enable_json=self.__enable_json,
        )

        logger = logging.getLogger(self.__logger)
        logger.setLevel(self.__level)
        logger.addHandler(logging.StreamHandler(sys.stdout))
