from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(init=True)
class BaseModel:
    id: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    @classmethod
    def from_raw_data(cls, raw_data: list | tuple) -> list:
        return [cls.from_row(row) for row in raw_data]

    @classmethod
    def from_row(cls, row: "BaseModel") -> "BaseModel" | None:
        return cls(**row._asdict()) if row else None  # pylint: disable=W0212

    def to_query_dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items() if value is not None}

    def _asdict(self) -> dict:
        return self.to_query_dict()
