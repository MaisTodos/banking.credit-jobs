from abc import ABC, abstractmethod


class IImportCreditInfoUseCase(ABC):
    @abstractmethod
    def perform(self):
        pass
