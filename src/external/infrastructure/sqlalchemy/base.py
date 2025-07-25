from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.external.error import InfrastructureException
from src.external.port.infrastructure.sql import ISqlBaseInfrastructure


class SqlInfrastructure(ISqlBaseInfrastructure):
    def __init__(self, connect_args: str, echo: bool):
        self.__engine = create_async_engine(
            "postgresql+psycopg://",
            pool_size=5,
            max_overflow=5,
            echo=echo,
            connect_args=connect_args,
        )
        self.__session_maker = async_sessionmaker(bind=self.__engine)

    def __session_factory(self):
        return self.__session_maker()

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        session = None
        try:
            session = self.__session_factory()
            yield session
        except Exception as error:
            await session.rollback()
            raise InfrastructureException(
                tag="external.infra.sql.database_error",
                original_error=error,
            ) from error
        finally:
            await session.close()
