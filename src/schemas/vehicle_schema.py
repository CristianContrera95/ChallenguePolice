from typing import List, Optional
from pydantic import BaseModel, EmailStr


VEHICLE_COLLECTION = 'vehicle'


class VehicleSchema(BaseModel):
    """Vehicle model"""
    plate_number: str
    model: str
    color: str
    person_owner: EmailStr


class VehicleResponseSchema(VehicleSchema):
    _id: Optional[str] = '0'


class VehiclesResponseSchema(BaseModel):
    vehicles: List[VehicleResponseSchema]
