import json
from collections.abc import Callable
from contextlib import asynccontextmanager
from unittest.mock import AsyncMock, patch

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.external.infrastructure.cache.redis_cache import RedisCacheClient
from src.external.model.sql.base import Base
from src.external.setting.config import CERT_PATH, SSL_MODE
from src.external.setting.environment import env
from src.main import app
from tests.integration.stub.sql_infra.sql_alchemy import SqlSpecStubInfra


@pytest.fixture
@asynccontextmanager
async def httpx_test_client():
    # TODO might need to review this later, app is not FastAPI app, don't know if there will be one
    client = AsyncClient(transport=ASGITransport(app=app), base_url="http://testserver")
    yield client
    await client.aclose()


@pytest.fixture
def model_factory() -> Callable:
    async def closure(model: Base, session: AsyncSession) -> Base:
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


@pytest.fixture(scope="module")
def vcr_config() -> dict:
    return {
        "ignore_localhost": True,
        "ignore_hosts": [
            "testserver",
            "dynamodb",
            "redis",
            "moto",
            "postgres",
            "localhost",
        ],
        "filter_headers": [
            ("token", "JWT_TOKEN"),
            ("authorization", "ANY"),
            ("Authorization", "ANY"),
        ],
        "filter_post_data_parameters": [
            ("client_id", "fake_client_id"),
            ("client_secret", "fake_client_secret"),
        ],
        "before_record_response": response_body_replace(
            [
                ("token", "ANY_TOKEN"),
                ("access_token", "ANY_ACCESS_TOKEN"),
            ],
        ),
        "record_mode": "once",
    }


def response_body_replace(items: list) -> Callable:
    def before_record_response(response: dict) -> dict:
        request_httpx = response.get("http_version")
        try:
            if request_httpx:
                body = json.loads(response["content"])
            else:
                body = json.loads(response["body"]["string"])
        except (json.decoder.JSONDecodeError, UnicodeDecodeError):
            return response

        for item in items:
            field, repl = item[0], item[1]
            if type(body) is dict and body.get(field):
                body[field] = repl
            if request_httpx:
                response["content"] = json.dumps(body)
            else:
                response["body"]["string"] = json.dumps(body).encode("utf-8")
        return response

    return before_record_response


@pytest.fixture
def mock_cache_redis():
    with patch.object(
        RedisCacheClient,
        "get_cached_data",
        new_callable=AsyncMock,
        return_value=None,
    ):
        yield
