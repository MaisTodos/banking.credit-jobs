from logging import getLogger

from witch_doctor import WitchDoctor

from src.application.port.service.business_credit_unit_of_work import (
    IBusinessCreditUnitOfWork,
)
from src.application.port.use_case.credit.persist_credit_info import (
    IPersistCreditInfoUseCase,
)
from src.external.model.sql.credit.business_credit import BusinessCreditModel

logger = getLogger("application.use_cases.credit.persist_credit_info")


class PersistCreditInfoUseCase(IPersistCreditInfoUseCase):
    @WitchDoctor.injection
    def __init__(self, unit_of_work: IBusinessCreditUnitOfWork):
        self.__unit_of_work = unit_of_work

    def convert_to_database_model(self, credit_info: list) -> list:
        return [
            BusinessCreditModel.create_from_entity(entity)
            for entity in credit_info[:10]
        ]

    async def perform(self, credit_entities: list) -> None:
        if not credit_entities:
            logger.warning("No credit data was passed to upsert", extra=credit_entities)
            return

        credit_models = self.convert_to_database_model(credit_entities)
        async with self.__unit_of_work as uow:
            _ = await uow.business_credit_repository.upsert_credit_information(
                credit_models
            )
