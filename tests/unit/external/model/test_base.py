import datetime
import uuid

from src.external.model.base import BaseModel


def test_create_base_model():
    timestamp = datetime.datetime.now(tz=datetime.UTC)
    test_id = uuid.uuid4()

    model = BaseModel(
        id=test_id,
        created_at=timestamp,
        updated_at=timestamp,
    )

    assert isinstance(model, BaseModel)
    assert model.id == test_id
    assert model.created_at == model.updated_at == timestamp


def test_base_model_asdict():
    timestamp = datetime.datetime.now(tz=datetime.UTC)
    test_id = uuid.uuid4()
    query_dict = {
        "id": test_id,
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    model = BaseModel(
        id=test_id,
        created_at=timestamp,
        updated_at=timestamp,
    )

    assert model.to_query_dict() == model._asdict() == query_dict

    model.updated_at = None
    assert "updated_at" not in model.to_query_dict()
