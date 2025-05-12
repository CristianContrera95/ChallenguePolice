from pydantic import EmailStr
from fastapi import APIRouter, Depends

from api.views.login import get_current_account
from schemas import (PersonSchema, OfficialSchema, TicketSchema, TicketResponseSchema, TicketsResponseSchema)
from core.ticket import get_tickets_by_email, save_ticket


router = APIRouter()


# Models
@router.get("/get_tickets", description="Returns the model list")
async def get_tickets(email: str | EmailStr = None):
    return await get_tickets_by_email(email=email)


@router.post("/load_ticket", description="Create a new ticket")
async def new_ticket(model: TicketSchema, official: OfficialSchema = Depends(get_current_account)):
    model = await save_ticket(model, official)
    return {"ticket_id": str(model.inserted_id)}
