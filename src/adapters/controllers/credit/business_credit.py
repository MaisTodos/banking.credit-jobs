from witch_doctor import WitchDoctor

from src.application.port.facades.credit.business_credit import IBusinessCreditFacade


class BusinessCreditController:
    @WitchDoctor.injection
    def __init__(self, business_credit_facade: IBusinessCreditFacade):
        self.__business_credit = business_credit_facade

    def update_credit_info(self):
        credit_info = self.__business_credit.import_credit_info()

        self.__business_credit.persist_credit_info(credit_info)
