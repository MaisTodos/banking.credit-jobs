from sqlalchemy import Column, Numeric, Unicode
from sqlalchemy_utils import UUIDType

from src.external.model.base import BaseModel


class BusinessCredit(BaseModel):
    business_credit_id = Column(UUIDType(binary=False), nullable=False)
    document = Column(Unicode(14), nullable=False, index=True)
    cgr = Column(Numeric(precision=10, scale=2), nullable=False)
    qia = Column(Numeric(precision=10, scale=2), nullable=False)
