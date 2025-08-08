import uuid

import pytest

from src.domain.entity.credit import BusinessCreditEntity


@pytest.fixture
def list_credit_limit_business_entities():
    entities_params = [
        {"id": uuid.uuid4(), "document": 12345678901230, "qia": 0.00, "cgr": 16400.48},
        {"id": uuid.uuid4(), "document": 12345678901231, "qia": 0.00, "cgr": 28.52},
        {"id": uuid.uuid4(), "document": 12345678901232, "qia": 0.00, "cgr": 0.00},
        {"id": uuid.uuid4(), "document": 12345678901233, "qia": 0.00, "cgr": 173903.19},
        {"id": uuid.uuid4(), "document": 12345678901234, "qia": 0.00, "cgr": 126422.91},
    ]

    entities = [BusinessCreditEntity.create(**params) for params in entities_params]
    return entities
