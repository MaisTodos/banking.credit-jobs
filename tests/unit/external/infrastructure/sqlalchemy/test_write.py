import pytest

from src.external.error import InfrastructureException
from src.external.infrastructure.sqlalchemy.base import SqlInfrastructure
from src.external.port.infrastructure.sql import ISqlInfrastructureWrite
from tests import patcher
from tests.unit.stub.sqlalchemy.session import SqlAlchemyStubAsyncSession


@pytest.mark.unit
class TestSqlAlchemyWriteInfra:
    def test_sqlalchemy_infra_write_instance(self, sql_infra_write):
        assert isinstance(sql_infra_write, SqlInfrastructure)
        assert isinstance(sql_infra_write, ISqlInfrastructureWrite)
        assert len(sql_infra_write.__dict__) == 2

    @pytest.mark.asyncio
    async def test_sql_alchemy_write_infra_success(self, sql_infra_write):
        async with sql_infra_write.session() as session:
            response = session.add(object())
            await session.commit()
            assert response is None

        assert session.commits_called == 1
        assert session.rollbacks_called == 0
        assert session.closed_connections == 1

    @pytest.mark.asyncio
    async def test_sql_alchemy_write_infra_exception(self, sql_infra_write):
        with pytest.raises(InfrastructureException) as error:
            with patcher(
                (
                    SqlAlchemyStubAsyncSession,
                    "commit",
                    {"side_effect": Exception()},
                ),
            ):
                async with sql_infra_write.session() as session:
                    _ = session.add(object())
                    await session.commit()

        assert session.rollbacks_called == 1
        assert session.closed_connections == 1
        assert error.value.tag == "external.infra.sql.database_error"
