from abc import ABC, abstractmethod


class IBusinessCreditFacade(ABC):
    @abstractmethod
    def import_credit_info(self):
        pass

    @abstractmethod
    async def persist_credit_info(self, credit_info: list):
        pass
