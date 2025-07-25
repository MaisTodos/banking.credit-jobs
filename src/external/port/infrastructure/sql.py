from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession


class ISqlBaseInfrastructure(ABC):
    @abstractmethod
    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        pass


class ISqlInfrastructureWrite(ISqlBaseInfrastructure, ABC):
    pass


class ISqlInfrastructureRead(ISqlBaseInfrastructure, ABC):
    pass
