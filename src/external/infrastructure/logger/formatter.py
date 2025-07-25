from copy import deepcopy
from typing import Any, ClassVar

import json_logging


class CreditApiJsonFormatter(json_logging.JSONLogFormatter):
    HTTP_SENSITIVE_KEYS: ClassVar[list[str]] = [
        "Authorization",
        "access_token",
        "client_id",
    ]
    SENSITIVE_KEYS: ClassVar[list[str]] = HTTP_SENSITIVE_KEYS

    def _format_log_object(self, record: Any, request_util: Any) -> dict:
        json_log_object = super()._format_log_object(record, request_util)
        context_data = None  # get_all_context()

        sensitive_json_log = self.__remove_sensitive_data_recursive(
            data=json_log_object,
            sensitive_keys=self.SENSITIVE_KEYS,
        )

        if context_data:
            if "aws_request_id" in context_data:
                sensitive_json_log["aws_request_id"] = context_data["aws_request_id"]

            if "end_to_end_id" in context_data:
                sensitive_json_log["end_to_end_id"] = context_data["end_to_end_id"]

        return sensitive_json_log

    @staticmethod
    def __remove_sensitive_data_recursive(
        data: dict | list | tuple,
        sensitive_keys: list[str],
        replace_value: str = "*****",
    ) -> dict:
        data_copy = deepcopy(data)

        if isinstance(data_copy, dict):
            for key in data_copy:
                if key in sensitive_keys and isinstance(data_copy[key], str):
                    data_copy[key] = replace_value
                else:
                    data_copy[key] = (
                        CreditApiJsonFormatter.__remove_sensitive_data_recursive(
                            data_copy[key],
                            sensitive_keys,
                            replace_value,
                        )
                    )
        elif isinstance(data_copy, list):
            data_copy = [
                CreditApiJsonFormatter.__remove_sensitive_data_recursive(
                    item,
                    sensitive_keys,
                    replace_value,
                )
                for item in data_copy
            ]
        elif isinstance(data_copy, tuple):
            data_copy = tuple(
                CreditApiJsonFormatter.__remove_sensitive_data_recursive(
                    item,
                    sensitive_keys,
                    replace_value,
                )
                for item in data_copy
            )

        return data_copy
