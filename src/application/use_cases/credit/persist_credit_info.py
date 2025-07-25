from src.application.port.use_case.credit.persist_credit_info import (
    IPersistCreditInfoUseCase,
)


class PersistCreditInfoUseCase(IPersistCreditInfoUseCase):
    def __init__(self):
        pass

    def perform(self, credit_info):
        credit_info = credit_info or []
        for line in credit_info:
            print(line)
