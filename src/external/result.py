from typing import Generic, Self, TypeVar

T = TypeVar("T")
E = TypeVar("E")


class Result(Generic[T, E]):
    def __init__(
        self,
        success: bool,
        value: T | None = None,
        error: E | None = None,
    ):
        self.value = value
        self.error = error
        self.__is_success = success

    @property
    def is_success(self) -> bool:
        return self.__is_success

    @property
    def is_failure(self) -> bool:
        return not self.__is_success

    @classmethod
    def ok(cls, value: T) -> Self:
        return cls(value=value, success=True)

    @classmethod
    def fail(cls, error: E = None) -> Self:
        return Result(error=error, success=False)
