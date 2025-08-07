import uuid

import pytest

from src.domain.entity.credit import BusinessCreditEntity
from src.external.model.sql.credit.business_credit import BusinessCreditModel


@pytest.fixture
def list_credit_entities() -> list[BusinessCreditEntity]:
    return [
        BusinessCreditEntity.create(
            id=uuid.uuid4(),
            document=12345678901234,
            cgr=3.14,
            qia=42.67,
        ),
        BusinessCreditEntity.create(
            id=uuid.uuid4(),
            document=12345678901235,
            cgr=0,
            qia=0,
        ),
    ]


@pytest.fixture
def list_credit_models(
    list_credit_entities: list[BusinessCreditEntity],
) -> list[BusinessCreditModel]:
    return [
        BusinessCreditModel.create_from_entity(entity)
        for entity in list_credit_entities
    ]
