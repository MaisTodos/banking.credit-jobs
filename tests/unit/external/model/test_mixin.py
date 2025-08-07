from decimal import Decimal

import pytest

from src.external.model.mixin.decimal_mixin import DecimalMixin


@pytest.mark.unit
class TestDecimalMixin:
    @pytest.mark.parametrize(
        ("_value", "_expected"),
        [
            (None, None),
            ("100.00", Decimal("100.00")),
            (100.1, Decimal("100.10")),
            (100, Decimal("100.00")),
        ],
    )
    def test_format_to_decimal(self, _value, _expected):
        assert DecimalMixin._format_to_decimal(_value) == _expected
