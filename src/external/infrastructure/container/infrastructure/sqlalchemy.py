from collections.abc import Callable

from witch_doctor import InjectionType

from src.external.infrastructure.sqlalchemy.read import SqlAlchemyInfrastructureRead
from src.external.infrastructure.sqlalchemy.write import SqlAlchemyInfrastructureWrite
from src.external.port.infrastructure.sql import (
    ISqlInfrastructureRead,
    ISqlInfrastructureWrite,
)
from src.external.setting.config import CERT_PATH, ECHO, SSL_MODE
from src.external.setting.environment import env


def register_sqlalchemy_dependencies(container: Callable) -> None:
    container(
        ISqlInfrastructureWrite,
        SqlAlchemyInfrastructureWrite,
        InjectionType.SINGLETON,
        args=[
            {
                "host": env.DATABASE_WRITE_HOST,
                "user": env.DATABASE_WRITE_USER,
                "port": env.DATABASE_WRITE_PORT,
                "password": env.DATABASE_WRITE_PASSWORD,
                "dbname": env.DATABASE_WRITE_NAME,
                "sslmode": SSL_MODE,
                "sslrootcert": CERT_PATH,
            },
            ECHO,
        ],
    )

    container(
        ISqlInfrastructureRead,
        SqlAlchemyInfrastructureRead,
        InjectionType.SINGLETON,
        args=[
            {
                "host": env.DATABASE_READ_HOST,
                "user": env.DATABASE_READ_USER,
                "port": env.DATABASE_READ_PORT,
                "password": env.DATABASE_READ_PASSWORD,
                "dbname": env.DATABASE_READ_NAME,
                "sslmode": SSL_MODE,
                "sslrootcert": CERT_PATH,
            },
            ECHO,
        ],
    )
