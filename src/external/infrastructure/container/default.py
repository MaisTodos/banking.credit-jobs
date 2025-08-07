from witch_doctor import InjectionType, WitchDoctor

from src.external.infrastructure.container.credit.business_credit import (
    register_business_credit_dependencies,
)
from src.external.infrastructure.container.infrastructure.sqlalchemy_ioc import (
    register_sqlalchemy_dependencies,
)
from src.external.infrastructure.i18n.python_i18n import PythonI18nInfra
from src.external.port.infrastructure.i18n import Ii18nInfrastructure


class ContainerDefault:
    @classmethod
    def create_ioc_container(cls) -> None:
        container = cls()
        container()

    def __call__(self):
        container = WitchDoctor.container("prod")

        register_sqlalchemy_dependencies(container)
        register_business_credit_dependencies(container)

        container(Ii18nInfrastructure, PythonI18nInfra, InjectionType.SINGLETON)
