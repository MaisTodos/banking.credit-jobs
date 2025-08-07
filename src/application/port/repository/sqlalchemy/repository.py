from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class IRepositoryWrite(ABC, Generic[T]):
    @abstractmethod
    def create(self, obj_in: T) -> T:
        pass

    @abstractmethod
    def delete(self, obj_in: T) -> T:
        pass

    @abstractmethod
    def create_all(self, obj_in: T) -> T:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> T:
        pass
