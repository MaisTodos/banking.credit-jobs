import uuid
from collections.abc import Callable
from datetime import datetime
from pathlib import Path

import i18n
import pytest
from _pytest.fixtures import FixtureRequest
from witch_doctor import WitchDoctor

from src.external.infrastructure.container.default import ContainerDefault
from src.external.setting.environment import Environment, env
from src.main import PATH_TRANSLATOR

path = Path(__file__).resolve()
env_file = Path(path.parents[1]) / ".env-test"


@pytest.fixture
def is_valid_uuid() -> Callable:
    def closure(uuid_to_test: uuid.UUID | None = None, version: int = 4) -> bool:
        try:
            _ = uuid.UUID(uuid_to_test, version=version)
            return True
        except ValueError:
            return False

    return closure


@pytest.fixture
def is_valid_iso_format_datetime() -> Callable:
    def closure(datetime_str: str | None = None):
        try:
            datetime.fromisoformat(datetime_str)
            return True
        except (TypeError, ValueError):
            return False

    return closure


@pytest.fixture(scope="session", autouse=True)
def configure_test_env(request: FixtureRequest) -> None:  # noqa: ARG001
    test_env = Environment(_env_file=env_file)
    env.__dict__ = test_env.__dict__
    i18n.set("file_format", "json")
    i18n.set("locale", "pt_BR")
    i18n.load_path.append(PATH_TRANSLATOR)
    ContainerDefault.create_ioc_container()
    WitchDoctor.load_container("prod")


@pytest.fixture
def default_header() -> dict:
    return {
        "x-end-to-end": "2a12e6c8-48b8-4ebc-a83d-ba7bc0c07376",
        "aws_request_id": "2a12e6c8-48b8-4ebc-a83d-ba7bc0c07376",
        "user_id": "550e8400-e29b-41d4-a716-446655440001",
        "membership_id": "2a12e6c8-48b8-4ebc-a83d-ba7bc0c07376",
        "account_id": "7d58cced-d55f-4cbf-a686-b45f32e144c2",
        "account_branch": "1234",
        "account_number": "567890",
        "account_name": "Esquilo da Silva LTDA",
        "account_document": "54110417000136",
    }


@pytest.fixture
def receivables_advance_header(default_header: default_header) -> dict:
    default_header.update(
        {
            "merchant_id": "1234567890",
        },
    )

    return default_header
