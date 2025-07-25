from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Either:
    has_errors: bool
    messages: list[str] | list[dict]
    result: any

    @classmethod
    def create(
        cls,
        has_errors: bool,
        messages: list[str] | list[dict],
        result: any,
    ) -> Self:
        return cls(has_errors=has_errors, messages=messages, result=result)
