import pytest
from app.models.shared import UUIDString
from pydantic import BaseModel, Field, ValidationError

def test_UUID_string():

    #define a pydantic model that uses the UUIDString custom type
    class TestModel(BaseModel):
        id: UUIDString

    #valid uuid string
    t1 = TestModel(
        id='75442486-0878-440c-9db1-a7006c25a39f'
    )
    assert t1.id == '75442486-0878-440c-9db1-a7006c25a39f'

    #invalid uuid string
    with pytest.raises(ValidationError):
        t1 = TestModel(
            id=0xcafebabe
        )

    #invalid uuid string
    with pytest.raises(ValidationError):
        t1 = TestModel(
            id='75442486-0878-440c-9db1-a7006c25a3XX'
        )

    #schema has an example description
    schema = TestModel.schema()
    assert len(schema['properties']['id']['examples']) > 0
