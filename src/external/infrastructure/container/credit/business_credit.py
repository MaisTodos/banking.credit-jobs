from collections.abc import Callable

from witch_doctor import InjectionType

from src.application.facades.credit.business_credit import BusinessCreditFacade
from src.application.port.facades.credit.business_credit import IBusinessCreditFacade
from src.application.port.use_case.credit.import_credit_info import (
    IImportCreditInfoUseCase,
)
from src.application.port.use_case.credit.persist_credit_info import (
    IPersistCreditInfoUseCase,
)
from src.application.use_cases.credit.import_credit_info import ImportCreditInfoUseCase
from src.application.use_cases.credit.persist_credit_info import (
    PersistCreditInfoUseCase,
)
from src.external.port.infrastructure.aws import IS3DownloadInfrastructure
from src.external.repository.aws.download import S3BaseDownloadInfrastructure


def register_business_credit_dependencies(container: Callable) -> None:
    container(
        IImportCreditInfoUseCase,
        ImportCreditInfoUseCase,
        InjectionType.SINGLETON,
    )

    container(
        IPersistCreditInfoUseCase,
        PersistCreditInfoUseCase,
        InjectionType.SINGLETON,
    )

    container(
        IBusinessCreditFacade,
        BusinessCreditFacade,
        InjectionType.SINGLETON,
    )

    container(
        IS3DownloadInfrastructure,
        S3BaseDownloadInfrastructure,
        InjectionType.SINGLETON,
    )
