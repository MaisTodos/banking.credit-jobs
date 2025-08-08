import uuid
from datetime import datetime
from typing import ClassVar

from sqlalchemy import Column, DateTime
from sqlalchemy_utils import UUIDType

from src.external.model.sql import DeclarativeBase


class BaseSQLModel(DeclarativeBase):
    __abstract__ = True
    __table_args__: ClassVar = {"mysql_engine": "InnoDB"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
