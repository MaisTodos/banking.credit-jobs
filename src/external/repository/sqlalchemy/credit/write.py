import datetime

from sqlalchemy import Tuple, or_
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.sql.dml import ReturningInsert

from src.domain.ports.repository.sql.credit.write import IBusinessCreditRepositoryWrite
from src.external.error import InfrastructureException, RepositoryException
from src.external.model.sql.credit.business_credit import BusinessCreditModel
from src.external.repository.sqlalchemy.write import SQLAlchemyRepositoryWrite


class BusinessCreditRepositoryWrite(
    SQLAlchemyRepositoryWrite[BusinessCreditModel],
    IBusinessCreditRepositoryWrite[BusinessCreditModel],
):
    def __get_models_as_dicts(
        self, credit_info: list[BusinessCreditModel]
    ) -> list[dict]:
        return [info.row for info in credit_info]

    def __build_upsert_statement(self, values: list[dict]) -> ReturningInsert[Tuple]:
        stmt = insert(self._model).values(values)

        any_limit_has_changed = or_(
            self._model.cgr != stmt.excluded.cgr, self._model.qia != stmt.excluded.qia
        )
        stmt = stmt.on_conflict_do_update(
            constraint="credit_limit_business_document_key",
            set_={
                "cgr": stmt.excluded.cgr,
                "qia": stmt.excluded.qia,
                "updated_at": datetime.datetime.now(tz=datetime.UTC),
            },
            where=(any_limit_has_changed),
        )

        return stmt

    async def upsert_credit_information(
        self,
        credit_models: list[BusinessCreditModel],
    ):
        try:
            async with self._sql_infra_write.session() as session:
                values = self.__get_models_as_dicts(credit_models)

                stmt = self.__build_upsert_statement(values)

                _ = await session.execute(stmt)
                await session.commit()

        except InfrastructureException as error:
            raise RepositoryException(
                tag="external.repository.sql_alchemy.credit.write.fail_to_add_business_credit_information",
                original_error=error,
            ) from error
