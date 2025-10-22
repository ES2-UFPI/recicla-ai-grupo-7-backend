from pydantic import BaseModel,Field, field_validator
from datetime import datetime

class RecyclableMaterial(BaseModel):
    type: str = Field(..., description="Type of recyclable material", examples=["plastic", "paper", "glass"])
    description: str | None = Field(default=None, description="Description of the recyclable material")

    model_config = {
        "from_attributes": True
    }

class RecyclableMaterialOut(BaseModel):
    id: str
    type: str = Field(..., description="Type of recyclable material", examples=["plastic", "paper", "glass"])
    description: str | None = Field(default=None, description="Description of the recyclable material")

    model_config = {
        "from_attributes": True
    }

class RecyclableMaterialItem(BaseModel):
    material_id: str = Field(..., description="ID of the recyclable material")
    quantity: int = Field(..., gt=0, description="Quantity of the material items")
    weight_kg: float | None = Field(default=None, description="Weight of the material items in kilograms")

    model_config = {
        "from_attributes": True
    }


class PickupRequest(BaseModel):
    address_id: str
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
    
class PickupRequestOut(BaseModel):
    id: str
    producer_id: str
    address_id: str
    scheduled_time: datetime
    items: list[RecyclableMaterialItem] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }



