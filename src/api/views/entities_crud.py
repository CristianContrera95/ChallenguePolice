from fastapi import APIRouter, Depends

from api.views.login import get_current_account
from schemas import (PersonSchema, OfficialSchema, OfficialsResponseSchema, PersonsResponseSchema,
                     VehicleSchema, VehiclesResponseSchema, VehicleResponseSchema)
from core.entities_crud import (list_officials, save_official, drop_official, list_persons,
                                save_person, drop_person,list_vehicles, save_vehicle, drop_vehicle)


router = APIRouter(dependencies=[])


# Officials
@router.get("/get_officials", response_model=OfficialsResponseSchema, description="Returns the officials list")
async def get_officials(skip: int = 0, limit: int = 10):
    return await list_officials(skip, limit)


@router.post("/new_official", description="Create a new official")
async def new_official(official: OfficialSchema):
    official = await save_official(official)
    return {"official_id": str(official.inserted_id)}


@router.delete("/delete_official", description="delete a official")
async def delete_official(official: OfficialSchema):
    await drop_official(official)
    return {"status": "ok"}


# Persons
@router.get("/get_persons", response_model=PersonsResponseSchema, description="Returns the persons list")
async def get_persons(skip: int = 0, limit: int = 10):
    return await list_persons(skip, limit)


@router.post("/new_person", description="Create a new persons")
async def new_person(person: PersonSchema):
    person = await save_person(person)
    return {"person_id": str(person.inserted_id)}


@router.delete("/delete_person", description="delete a persons")
async def delete_person(person: PersonSchema):
    await drop_person(person)
    return {"status": "ok"}


# Vehicles
@router.get("/get_vehicles", response_model=VehiclesResponseSchema, description="Returns the vehicles list")
async def get_vehicles(skip: int = 0, limit: int = 10):
    return await list_vehicles(skip, limit)


@router.post("/new_vehicle", description="Create a new vehicle")
async def new_person(vehicle: VehicleSchema):
    vehicle = await save_vehicle(vehicle)
    return {"vehicle_id": str(vehicle.inserted_id)}


@router.delete("/delete_vehicle", description="delete a vehicle")
async def delete_vehicle(vehicle: VehicleSchema):
    await drop_vehicle(vehicle)
    return {"status": "ok"}
