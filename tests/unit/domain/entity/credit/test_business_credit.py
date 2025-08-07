from decimal import Decimal

import pydantic_core
import pytest

from src.domain.entity.credit import BusinessCreditEntity
from src.domain.error.error import DomainException


def test_create_business_credit_entity_successful(base_list_business_credit_limit):
    entity = BusinessCreditEntity.create(**base_list_business_credit_limit)
    base_list_business_credit_limit["document"] = str(
        base_list_business_credit_limit["document"]
    )
    base_list_business_credit_limit["cgr"] = Decimal(
        str(base_list_business_credit_limit["cgr"])
    )
    base_list_business_credit_limit["qia"] = Decimal(
        str(base_list_business_credit_limit["qia"])
    )

    assert entity.as_dict == base_list_business_credit_limit


def test_create_business_credit_entity_failed(base_list_business_credit_limit):
    bad_parameters = base_list_business_credit_limit.copy()
    bad_parameters["document"] = None

    with pytest.raises(DomainException) as error:
        _ = BusinessCreditEntity.create(**bad_parameters)

    assert error.value.tag == "domain.entity.credit.fail_to_validate"
    assert error.value.details[0]["loc"] == ("document",)
    assert error.value.details[0]["msg"] == "Input should be a valid string"
    assert isinstance(
        error.value.original_error, pydantic_core._pydantic_core.ValidationError
    )
