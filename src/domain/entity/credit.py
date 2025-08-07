import logging
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ValidationError

from src.domain.error.error import DomainException
from src.external.model.mixin.decimal_mixin import DecimalMixin

logger = logging.getLogger("domain.entity.credit")


class BusinessCreditEntity(DecimalMixin, BaseModel):
    id: UUID
    document: str
    cgr: Decimal
    qia: Decimal

    @classmethod
    def create(
        cls,
        id: UUID,
        document: str | int,
        cgr: float,
        qia: float,
    ) -> "BusinessCreditEntity":
        try:
            if isinstance(document, int):
                document = str(document)
            return cls(
                id=id,
                document=document,
                cgr=cls._format_to_decimal(cgr),
                qia=cls._format_to_decimal(qia),
            )
        except ValidationError as error:
            logger.debug(
                msg=f"fail to create {cls.__name__}",
                extra={
                    "props": {"validation_errors": error.errors()},
                },
            )
            raise DomainException(
                tag="domain.entity.credit.fail_to_validate",
                details=error.errors(),
                original_error=error,
            ) from error

    @property
    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "document": self.document,
            "qia": self.qia,
            "cgr": self.cgr,
        }

    def __repr__(self):
        return (
            f"<BusinessCreditEntity[{self.document}] qia [{self.qia}] cgr [{self.cgr}]>"
        )
