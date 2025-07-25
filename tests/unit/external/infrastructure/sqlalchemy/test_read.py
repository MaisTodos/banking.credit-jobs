import pytest

from src.external.error import InfrastructureException
from src.external.infrastructure.sqlalchemy.base import SqlInfrastructure
from src.external.port.infrastructure.sql import ISqlInfrastructureRead
from tests import patcher
from tests.unit.stub.sqlalchemy.session import SqlAlchemyStubAsyncSession


@pytest.mark.unit
class TestSqlAlchemyReadInfra:
    def test_sqlalchemy_infra_read_instance(self, sql_infra_read):
        assert isinstance(sql_infra_read, SqlInfrastructure)
        assert isinstance(sql_infra_read, ISqlInfrastructureRead)
        assert len(sql_infra_read.__dict__) == 2

    @pytest.mark.asyncio
    async def test_sql_alchemy_read_infra_success(self, sql_infra_read):
        async with sql_infra_read.session() as session:
            executable = "select(model)"
            response = await session.scalars(executable)
            assert callable(response.all)
            assert callable(response.first)

        assert session.closed_connections == 1

    @pytest.mark.asyncio
    async def test_sql_alchemy_read_infra_exception(self, sql_infra_read):
        with pytest.raises(InfrastructureException) as error:
            with patcher(
                (
                    SqlAlchemyStubAsyncSession,
                    "scalars",
                    {"side_effect": Exception()},
                ),
            ):
                async with sql_infra_read.session() as session:
                    executable = "select(model)"
                    _ = await session.scalars(executable)

        assert session.closed_connections == 1
        assert session.rollbacks_called == 1
        assert error.value.tag == "external.infra.sql.database_error"
