from decimal import ROUND_HALF_UP, Decimal

from pydantic import BaseModel


class DecimalMixin(BaseModel):
    @classmethod
    def _format_to_decimal(
        cls,
        value: float | str | None,
        fmt: str = "0.00",
    ) -> Decimal | None:
        if value is None:
            return None
        return Decimal(str(value)).quantize(Decimal(fmt), rounding=ROUND_HALF_UP)
