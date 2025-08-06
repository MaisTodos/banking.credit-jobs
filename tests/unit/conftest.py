from unittest.mock import patch

import pytest

from src.external.infrastructure.sqlalchemy.read import SqlAlchemyInfrastructureRead
from src.external.infrastructure.sqlalchemy.write import SqlAlchemyInfrastructureWrite
from src.external.setting.config import CERT_PATH
from src.external.setting.environment import env
from tests.unit.stub.sqlalchemy.engine import SqlAlchemyStubAsyncEngine
from tests.unit.stub.sqlalchemy.session_maker import SqlAlchemyStubAsyncSessionMaker


@pytest.fixture(scope="session")
def test_write_connect_args() -> dict:
    return {
        "host": env.DATABASE_HOST,
        "user": env.DATABASE_USER,
        "password": env.DATABASE_PASSWORD,
        "dbname": env.DATABASE_NAME,
        "sslmode": "allow" if env.ENV == "local" else "verify-ca",
        "sslrootcert": CERT_PATH,
    }


@pytest.fixture(scope="session")
def test_read_connect_args() -> dict:
    return {
        "host": env.DATABASE_HOST,
        "user": env.DATABASE_USER,
        "password": env.DATABASE_PASSWORD,
        "dbname": env.DATABASE_NAME,
        "sslmode": "allow" if env.ENV == "local" else "verify-ca",
        "sslrootcert": CERT_PATH,
    }


@pytest.fixture
def sql_infra_write(test_write_connect_args: dict) -> SqlAlchemyInfrastructureWrite:
    with patch(
        "src.external.infrastructure.sqlalchemy.base.create_async_engine",
        return_value=SqlAlchemyStubAsyncEngine(),
    ):
        with patch(
            "src.external.infrastructure.sqlalchemy.base.async_sessionmaker",
            return_value=SqlAlchemyStubAsyncSessionMaker(),
        ):
            return SqlAlchemyInfrastructureWrite(test_write_connect_args, echo=True)


@pytest.fixture
def sql_infra_read(test_read_connect_args: dict) -> SqlAlchemyInfrastructureRead:
    with patch(
        "src.external.infrastructure.sqlalchemy.base.create_async_engine",
        return_value=SqlAlchemyStubAsyncEngine(),
    ):
        with patch(
            "src.external.infrastructure.sqlalchemy.base.async_sessionmaker",
            return_value=SqlAlchemyStubAsyncSessionMaker(),
        ):
            return SqlAlchemyInfrastructureRead(test_read_connect_args, echo=True)
