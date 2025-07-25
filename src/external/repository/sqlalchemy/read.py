import math
from typing import Any, TypeVar

from sqlalchemy import Select, desc, func
from sqlalchemy.future import select

from src.application.port.repository.sqlalchemy.repository import IRepositoryRead
from src.external.error import InfrastructureException, RepositoryException
from src.external.model.sql.base import Base
from src.external.model.sql.paginated import PaginatedResult
from src.external.port.infrastructure.sql import ISqlInfrastructureRead

T = TypeVar("T", bound=Base)


class SQLAlchemyRepositoryRead(IRepositoryRead[T]):
    def __init__(
        self,
        model: type[T],
        sql_infra_read: ISqlInfrastructureRead,
    ):
        self._model: type[T] = model
        self._sql_infra_read = sql_infra_read

    async def get_by_id(self, id: str) -> T:
        try:
            async with self._sql_infra_read.session() as session:
                statement = select(self._model).where(self._model.id == id)
                result = await session.execute(statement)
                return result.scalar_one()
        except InfrastructureException as error:
            raise RepositoryException(
                tag="external.repository.sql_alchemy.fail_get_by_id",
                original_error=error,
            ) from error

    async def list_paginated(self, page: int, page_size: int) -> PaginatedResult[T]:
        statement = select(self._model)
        return await self._list_paginated(statement, page, page_size)

    async def _list_paginated(
        self,
        statement: Select[Any],
        page: int,
        per_page: int,
    ) -> PaginatedResult[T]:
        try:
            async with self._sql_infra_read.session() as session:
                count_sub_query = statement.subquery()
                count_stmt = select(func.count()).select_from(count_sub_query)
                total_result = await session.execute(count_stmt)
                total: int = total_result.scalar_one()

                if per_page > 0:
                    total_pages = math.ceil(total / per_page)
                else:
                    total_pages = 1 if total > 0 else 0

                next_page = page + 1 if page < total_pages else None

                statement = self._desc_order_by_created_at(statement)
                statement = self._query_pagination(statement, page, per_page)
                result = await session.execute(statement)
                items: list[T] = result.scalars().all()

                return PaginatedResult(
                    items=items,
                    page=page,
                    per_page=per_page,
                    total=total,
                    total_pages=total_pages,
                    next_page=next_page,
                )

        except InfrastructureException as error:
            raise RepositoryException(
                tag="external.repository.sql_alchemy.fail_list_paginated",
                original_error=error,
            ) from error

    def _desc_order_by_created_at(self, statement: Select) -> Select:
        return statement.order_by(desc(self._model.created_at))

    @staticmethod
    def _query_pagination(statement: Select, page: int, page_size: int) -> Select:
        offset = 0 if page == 1 else (page - 1) * page_size
        limit = page_size
        return statement.offset(offset).limit(limit)
