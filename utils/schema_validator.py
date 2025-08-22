from pydantic import BaseModel, ValidationError
from typing import Type

def response_schema_validator(model: Type[BaseModel], data):
    try:
        return model.model_validate(data)
    except ValidationError as e:
        raise AssertionError(f"Schema validation failed:\n{e}")
