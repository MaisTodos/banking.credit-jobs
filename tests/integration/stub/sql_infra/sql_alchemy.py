import logging
from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncConnection, AsyncEngine, AsyncTransaction
from sqlalchemy.orm import declarative_base

from src.external.port.infrastructure.sql import ISqlBaseInfrastructure

logger = logging.getLogger("views")

Base = declarative_base()


class SqlSpecStubInfra(ISqlBaseInfrastructure):
    def __init__(
        self,
        engine: AsyncEngine,
        connection: AsyncConnection,
        transaction: AsyncTransaction,
        session_maker: async_sessionmaker,
    ):
        self.__engine = engine
        self.connection = connection
        self.transaction = transaction
        self.session_maker = session_maker
        self.sessions = []

    @classmethod
    async def create(cls, connect_args: str, echo: bool) -> Self:
        engine = create_async_engine(
            "postgresql+psycopg://",
            pool_size=1,
            max_overflow=1,
            echo=echo,
            connect_args=connect_args,
        )
        connection = await engine.connect()
        transaction = await connection.begin()
        session_maker = async_sessionmaker(bind=connection)
        return cls(engine, connection, transaction, session_maker)

    def session(self) -> AsyncSession:
        session = self.session_maker()
        self.sessions.append(session)
        return session

    async def close_sessions(self):
        for session in self.sessions:
            await session.close()
