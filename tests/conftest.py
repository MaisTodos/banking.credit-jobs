from pathlib import Path

import i18n
import pytest
from witch_doctor import WitchDoctor

from src.external.infrastructure.container.default import ContainerDefault
from src.external.setting.environment import Environment, env
from src.main import PATH_TRANSLATOR

path = Path(__file__).resolve()
env_file = Path(path.parents[1]) / ".env-test"


@pytest.fixture(scope="session", autouse=True)
def configure_test_env() -> None:
    test_env = Environment(_env_file=env_file)
    env.__dict__ = test_env.__dict__
    i18n.set("file_format", "json")
    i18n.set("locale", "pt_BR")
    i18n.load_path.append(PATH_TRANSLATOR)
    ContainerDefault.create_ioc_container()
    WitchDoctor.load_container("prod")
