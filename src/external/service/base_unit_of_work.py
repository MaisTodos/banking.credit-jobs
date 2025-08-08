import logging
from abc import abstractmethod
from typing import TypeVar

from sqlalchemy.orm import Session

from src.external.error import InfrastructureException, RepositoryException
from src.external.infrastructure.sqlalchemy.write import SqlAlchemyInfrastructure
from src.external.model.sql.base_sql import BaseSQLModel

T = TypeVar("T", bound=BaseSQLModel)
logger = logging.getLogger("external")


class BaseUnitOfWork:
    def __init__(self, infra_write: SqlAlchemyInfrastructure):
        self.__session = None
        self._infra_write = infra_write
        self.__session_context = None

    @abstractmethod
    def _create_repositories(self, session: Session):
        pass

    async def __aenter__(self):
        self.__session_context = self._infra_write.session()
        self.__session = await self.__session_context.__aenter__()
        self._create_repositories(self.__session)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):  # noqa: ANN001
        try:
            await self.__session_context.__aexit__(exc_type, exc_value, traceback)
        except InfrastructureException as error:
            raise RepositoryException(
                tag="external.repository.unit_of_work.fail_to_perform_write",
                original_error=error,
            ) from error

    async def commit(self):
        await self.__session.commit()

    async def refresh(self, obj_in: T):
        await self.__session.refresh(obj_in)
