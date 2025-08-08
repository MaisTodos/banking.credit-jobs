import pytest

from src.application.port.repository.sqlalchemy.repository import IRepositoryWrite
from src.external.model.sql.base_sql import BaseSQLModel
from src.external.repository.sqlalchemy.write import SQLAlchemyRepositoryWrite


@pytest.mark.unit
class TestRepositoryWrite:
    @pytest.mark.asyncio
    async def test_repository_instance(self, sql_infra_write):
        session_context = sql_infra_write.session()
        session = await session_context.__aenter__()

        repository = SQLAlchemyRepositoryWrite(
            model=BaseSQLModel,
            sql_infra_write=sql_infra_write,
            session=session,
        )

        await session_context.__aexit__(None, None, None)

        assert session.closed_connections == 1
        assert isinstance(repository, SQLAlchemyRepositoryWrite)
        assert issubclass(SQLAlchemyRepositoryWrite, IRepositoryWrite)
        assert callable(repository.create) is True
        assert callable(repository.delete) is True
        assert callable(repository.create_all) is True
