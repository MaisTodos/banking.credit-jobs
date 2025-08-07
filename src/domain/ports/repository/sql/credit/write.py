from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class IBusinessCreditRepositoryWrite(ABC, Generic[T]):
    @abstractmethod
    async def upsert_credit_information(
        self,
        credit_info: list[T],
    ) -> list[T]:
        pass
