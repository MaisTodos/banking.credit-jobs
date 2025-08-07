import uuid

import pytest


@pytest.fixture
def base_list_business_credit_limit():
    return {
        "id": uuid.uuid4(),
        "document": 12345678901234,
        "cgr": 3.14,
        "qia": 42.67,
    }
