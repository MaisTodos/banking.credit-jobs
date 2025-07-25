from abc import ABC


class IBusinessCreditFacade(ABC):
    def import_credit_info(self):
        pass

    def persist_credit_info(self, credit_info):
        pass
