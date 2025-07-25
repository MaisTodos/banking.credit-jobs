from abc import ABC
from typing import TypeVar

from src.domain.ports.repository.sql.repository import IRepositoryWrite

T = TypeVar("T")


class IBusinessCreditRepositoryWrite(IRepositoryWrite[T], ABC):
    def to_be_named(self, credit_info) -> None:
        pass
