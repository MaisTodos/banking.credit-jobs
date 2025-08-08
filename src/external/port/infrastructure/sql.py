from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession


class ISqlInfrastructure(ABC):
    @abstractmethod
    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        pass
