from witch_doctor import WitchDoctor

from src.application.port.facades.credit.business_credit import IBusinessCreditFacade
from src.application.port.use_case.credit.import_credit_info import (
    IImportCreditInfoUseCase,
)
from src.application.port.use_case.credit.persist_credit_info import (
    IPersistCreditInfoUseCase,
)


class BusinessCreditFacade(IBusinessCreditFacade):
    @WitchDoctor.injection
    def __init__(
        self,
        import_credit_info: IImportCreditInfoUseCase,
        persist_credit_info: IPersistCreditInfoUseCase,
    ) -> None:
        self.__import_credit_info = import_credit_info
        self.__persist_credit_info = persist_credit_info

    def import_credit_info(self):
        return self.__import_credit_info.perform()

    def persist_credit_info(self, credit_info):
        self.__persist_credit_info.perform(credit_info)
