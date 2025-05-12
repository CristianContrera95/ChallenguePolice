from fastapi import APIRouter
from api.views import login, ticket_view, entities_crud

api_router = APIRouter()
api_router.include_router(login.router, prefix="/auth", tags=["auth"],
                          responses={404: {"description": "Not found"}})
api_router.include_router(ticket_view.router, prefix="/ticket", tags=["ticket"],
                          responses={404: {"description": "Not found"}})
api_router.include_router(entities_crud.router, prefix="/entities", tags=["entities"],)

@api_router.get("/")
async def hello():
    return {"server": "Fuck Police API"}
