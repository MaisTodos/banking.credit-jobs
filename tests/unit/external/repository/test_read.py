import pytest

from src.application.port.repository.sqlalchemy.repository import IRepositoryRead
from src.external.model.sql.base import Base
from src.external.repository.sqlalchemy.read import SQLAlchemyRepositoryRead


@pytest.mark.unit
class TestRepositoryRead:
    def test_repository_instance(self, sql_infra_read):
        repository = SQLAlchemyRepositoryRead(
            model=Base,
            sql_infra_read=sql_infra_read,
        )

        assert isinstance(repository, SQLAlchemyRepositoryRead)
        assert issubclass(SQLAlchemyRepositoryRead, IRepositoryRead)
        assert callable(repository.get_by_id)
