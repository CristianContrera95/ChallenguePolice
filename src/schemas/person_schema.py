from typing import List, Optional
from pydantic import BaseModel, EmailStr


PERSON_COLLECTION = 'person'


class PersonSchema(BaseModel):
    """person model"""
    name: str
    email: EmailStr


class PersonResponseSchema(PersonSchema):
    id: Optional[str] = '0'


class PersonsResponseSchema(BaseModel):
    persons: List[PersonResponseSchema]
