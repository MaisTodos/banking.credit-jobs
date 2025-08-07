from collections.abc import Callable

from witch_doctor import InjectionType

from src.application.port.service.business_credit_unit_of_work import (
    IBusinessCreditUnitOfWork,
)
from src.external.infrastructure.sqlalchemy.write import SqlAlchemyInfrastructure
from src.external.port.infrastructure.sql import ISqlInfrastructure
from src.external.service.business_credit_unit_of_work import BusinessCreditUnitOfWork
from src.external.setting.config import CERT_PATH, ECHO, SSL_MODE
from src.external.setting.environment import env


def register_sqlalchemy_dependencies(container: Callable) -> None:
    container(
        ISqlInfrastructure,
        SqlAlchemyInfrastructure,
        InjectionType.SINGLETON,
        args=[
            {
                "host": env.DATABASE_HOST,
                "user": env.DATABASE_USER,
                "port": env.DATABASE_PORT,
                "password": env.DATABASE_PASSWORD,
                "dbname": env.DATABASE_NAME,
                "sslmode": SSL_MODE,
                "sslrootcert": CERT_PATH,
            },
            ECHO,
        ],
    )

    container(
        IBusinessCreditUnitOfWork,
        BusinessCreditUnitOfWork,
        InjectionType.SINGLETON,
    )
