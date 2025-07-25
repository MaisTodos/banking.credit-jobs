from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class IRepositoryRead(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: int) -> T:  
        pass


class IRepositoryWrite(ABC, Generic[T]):
    @abstractmethod
    def create(self, obj_in: T) -> T:
        pass

    @abstractmethod
    def delete(self, obj_in: T) -> T:
        pass

    @abstractmethod
    def update(self, obj_in: T) -> T:
        pass

    @abstractmethod
    def create_all(self, obj_in: T) -> T:
        pass

    @abstractmethod
    def get_by_id_and_lock_for_update(self, id: str) -> T:
        pass
