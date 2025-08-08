from abc import ABC, abstractmethod

from src.application.port.repository.sqlalchemy.repository import IRepositoryWrite
from src.external.model.sql.credit.business_credit import BusinessCreditModel


class IBusinessCreditUnitOfWork(ABC):
    @property
    @abstractmethod
    def business_credit_repository(self) -> IRepositoryWrite[BusinessCreditModel]:
        pass
