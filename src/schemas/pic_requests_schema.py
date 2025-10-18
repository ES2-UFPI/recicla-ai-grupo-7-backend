from pydantic import BaseModel,Field, field_validator
from datetime import datetime

class RecyclableMaterial(BaseModel):
    type: str
    description: str | None = None

    model_config = {
        "from_attributes": True
    }

class RecyclableMaterialOut(BaseModel):
    id: int
    type: str
    description: str | None = None

    model_config = {
        "from_attributes": True
    }

class RecyclableMaterialItem(BaseModel):
    id: int
    quantity: int
    weight_kg: float | None = None

    model_config = {
        "from_attributes": True
    }


class PickupRequest(BaseModel):
    producer_id: int
    address_id: int
    scheduled_time: datetime
    items: list[RecyclableMaterialItem] = Field(default_factory=list)


    model_config = {
        "from_attributes": True
    }


    @field_validator('scheduled_time')
    def validate_scheduled_time(cls, v):
        if v < datetime.now():
            raise ValueError("scheduled_time must be in the future")
        return v



