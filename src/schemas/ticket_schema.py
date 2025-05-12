from typing import List, Optional
from pydantic import BaseModel, EmailStr

from .official_schema import OfficialSchema
TICKET_COLLECTION = 'ticket'


class TicketSchema(BaseModel):
    """Databricks models"""
    license_plate: str
    timestamp: str
    comments: str
    official_number: int
    person_email: EmailStr


class TicketResponseSchema(TicketSchema):
    _id: Optional[str] = '0'


class TicketsResponseSchema(BaseModel):
    tickets: List[TicketResponseSchema]
