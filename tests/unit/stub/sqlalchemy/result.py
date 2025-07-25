from typing import Self


class SqlAlchemyStubAsyncResult:
    async def first(self) -> None:
        return None

    def all(self) -> list:
        return []

    def scalar_one(self) -> None:
        return None

    def scalars(self) -> Self:
        return self
