import datetime
from typing import ClassVar

from sqlalchemy import Column, Numeric, Unicode

from src.domain.entity.credit import BusinessCreditEntity
from src.external.model.sql.base_sql import BaseSQLModel


class BusinessCreditModel(BaseSQLModel):
    __table_args__: ClassVar[dict[str, str]] = {"schema": "credit"}
    __tablename__: str = "credit_limit_business"

    document = Column(Unicode(14), nullable=False, index=True, unique=True)
    cgr = Column(Numeric(precision=11, scale=2), nullable=False)
    qia = Column(Numeric(precision=11, scale=2), nullable=False)

    @classmethod
    def create_from_entity(
        cls, credit_data: BusinessCreditEntity
    ) -> "BusinessCreditModel":
        return cls(
            **credit_data.as_dict,
            created_at=datetime.datetime.now(tz=datetime.UTC),
            updated_at=datetime.datetime.now(tz=datetime.UTC),
        )

    @property
    def row(self) -> dict:
        return {
            "id": self.id,
            "document": self.document,
            "cgr": self.cgr,
            "qia": self.qia,
        }
