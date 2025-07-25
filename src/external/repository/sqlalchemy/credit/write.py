from sqlalchemy.dialects.postgresql import insert

from src.application.port.repository.sqlalchemy.account_merchant.write import (
    IAccountMerchantRepositoryWrite,
)
from src.external.error import InfrastructureException, RepositoryException
from src.external.model.sql.account_merchant.model import AccountMerchant
from src.external.repository.sqlalchemy.write import SQLAlchemyRepositoryWrite


class AccountMerchantRepositoryWrite(
    SQLAlchemyRepositoryWrite[AccountMerchant],
    IAccountMerchantRepositoryWrite[AccountMerchant],
):
    async def upsert_batch(
        self,
        account_merchants: list[AccountMerchant],
    ) -> list[AccountMerchant]:
        try:
            async with self._sql_infra_write.session() as session:
                values = [
                    account_merchant.row for account_merchant in account_merchants
                ]
                stmt = insert(self._model).values(values)

                stmt = stmt.on_conflict_do_update(
                    constraint="account_merchant_unique",
                    set_={"linked": stmt.excluded.linked},
                ).returning(self._model)

                result = await session.execute(stmt)
                return result.scalars().all()
        except InfrastructureException as error:
            raise RepositoryException(
                tag="external.repository.sql_alchemy.fail_upsert_account_merchants_batch",
                original_error=error,
            ) from error
