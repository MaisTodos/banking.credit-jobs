import logging
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.ports.repository.sql.repository import IRepositoryWrite
from src.external.model.base import BaseSQLModel
from src.external.port.infrastructure.sql import ISqlInfrastructureWrite

T = TypeVar("T", bound=BaseSQLModel)
logger = logging.getLogger("external")


class SQLAlchemyRepositoryWrite(IRepositoryWrite[T], Generic[T]):
    def __init__(
        self,
        model: type[T],
        sql_infra_write: ISqlInfrastructureWrite,
        session: AsyncSession,
    ):
        self._session = session
        self._model: T = model
        self._sql_infra_write = sql_infra_write

    async def create(self, obj_in: T) -> T:
        self._session.add(obj_in)
        return obj_in

    async def delete(self, obj_in: T) -> T:
        self._session.delete(obj_in)
        return obj_in

    async def create_all(self, obj_in: list[T]) -> list[T]:
        self._session.add_all(obj_in)
        return obj_in

    async def merge_and_update(self, obj_in: T) -> T:
        merged_obj = await self._session.merge(obj_in)
        await self._session.flush()
        return merged_obj

    async def get_by_id(self, id: str) -> T:
        statement = select(self._model).where(self._model.id == id)
        result = await self._session.execute(statement)
        return result.scalars().first()
