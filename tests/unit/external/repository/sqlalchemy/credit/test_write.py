import pytest

from src.application.use_cases.credit.persist_credit_info import (
    PersistCreditInfoUseCase,
)
from src.external.error import RepositoryException
from src.external.repository.sqlalchemy.credit.write import (
    BusinessCreditRepositoryWrite,
)
from tests import patcher


@pytest.mark.asyncio
async def test_upsert_business_credit_success(
    list_credit_entities,
    list_credit_models,
):
    with patcher(
        (
            BusinessCreditRepositoryWrite,
            "upsert_credit_information",
            {"return_value": list_credit_models},
        ),
    ) as mock:
        use_case = PersistCreditInfoUseCase()
        _ = await use_case.perform(list_credit_entities)

        business_credit_repository_mock = mock[0][1]
        business_credit_repository_mock.assert_called_once()


@pytest.mark.asyncio
async def test_upsert_business_credit_fail(list_credit_entities):
    with patcher(
        (
            BusinessCreditRepositoryWrite,
            "upsert_credit_information",
            {
                "side_effect": RepositoryException(
                    "external.repository.sql_alchemy.credit.write.fail_to_add_business_credit_information",
                ),
            },
        ),
    ) as mock:
        use_case = PersistCreditInfoUseCase()
        with pytest.raises(RepositoryException) as error:
            _ = await use_case.perform(list_credit_entities)

        business_credit_repository_mock = mock[0][1]
        business_credit_repository_mock.assert_called_once()

        assert (
            error.value.tag == "external.repository.unit_of_work.fail_to_perform_write"
        )
