from abc import ABC, abstractmethod


class Ii18nInfrastructure(ABC):
    @abstractmethod
    def translator(self, key: str) -> str:
        pass
