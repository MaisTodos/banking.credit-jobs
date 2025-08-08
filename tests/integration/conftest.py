from collections.abc import Callable
from contextlib import asynccontextmanager

import pytest
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.external.model.sql.base_sql import BaseSQLModel
from src.external.setting.config import CERT_PATH, SSL_MODE
from src.external.setting.environment import env
from tests.integration.stub.sql_infra.sql_alchemy import SqlSpecStubInfra


@pytest.fixture
def model_factory() -> Callable:
    async def closure(model: BaseSQLModel, session: AsyncSession) -> BaseSQLModel:
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return model

    return closure


@pytest.fixture
@asynccontextmanager
async def sql_infra_test():
    infra = await SqlSpecStubInfra.create(
        {
            "host": env.DATABASE_HOST,
            "user": env.DATABASE_USER,
            "port": env.DATABASE_PORT,
            "password": env.DATABASE_PASSWORD,
            "dbname": env.DATABASE_NAME,
            "sslmode": SSL_MODE,
            "sslrootcert": CERT_PATH,
        },
        True,
    )
    session_method = infra.session
    yield session_method

    await infra.transaction.rollback()
    await infra.transaction.close()
    await infra.close_sessions()
    await infra.connection.close()
