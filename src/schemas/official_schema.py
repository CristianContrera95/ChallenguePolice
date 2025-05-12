from typing import List, Optional
from pydantic import BaseModel


OFFICIAL_COLLECTION = 'official'


class OfficialSchema(BaseModel):
    """Sheriff model"""
    name: str
    number: int
    password: str


class OfficialResponseSchema(OfficialSchema):
    _id: Optional[str] = '0'


class OfficialsResponseSchema(BaseModel):
    officials: List[OfficialResponseSchema]
