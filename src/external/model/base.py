from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(init=True)
class BaseModel:
    id: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    @classmethod
    def from_raw_data(cls, raw_data):
        return [cls.from_row(row) for row in raw_data]

    @classmethod
    def from_row(cls, row):
        return cls(**row._asdict()) if row else None  # pylint: disable=W0212

    def to_query_dict(self):
        query_dict = {}
        for key, value in self.__dict__.items():
            if value is not None:
                query_dict[key] = value
        return query_dict

    def _asdict(self):
        return self.to_query_dict()
