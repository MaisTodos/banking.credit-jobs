from sqlalchemy.orm import Session
from witch_doctor import WitchDoctor

from src.application.port.repository.sqlalchemy.repository import IRepositoryWrite
from src.application.port.service.business_credit_unit_of_work import (
    IBusinessCreditUnitOfWork,
)
from src.external.model.sql.credit.business_credit import BusinessCreditModel
from src.external.port.infrastructure.sql import ISqlInfrastructure
from src.external.repository.sqlalchemy.credit.write import (
    BusinessCreditRepositoryWrite,
)
from src.external.service.base_unit_of_work import BaseUnitOfWork


class BusinessCreditUnitOfWork(IBusinessCreditUnitOfWork, BaseUnitOfWork):
    @WitchDoctor.injection
    def __init__(self, infra_write: ISqlInfrastructure):
        self.__business_credit_repository = None
        super().__init__(infra_write=infra_write)

    def _create_repositories(self, session: Session):
        self.__business_credit_repository = BusinessCreditRepositoryWrite(
            BusinessCreditModel,
            self._infra_write,
            session,
        )

    @property
    def business_credit_repository(self) -> IRepositoryWrite[BusinessCreditModel]:
        return self.__business_credit_repository
