from abc import ABC, abstractmethod


class IPersistCreditInfoUseCase(ABC):
    @abstractmethod
    async def perform(self):
        pass
