import pymongo
from click import open_file
from pyasn1.type.univ import Boolean
from pydantic import EmailStr

import core.exceptions as exceptions
from api import mongodb
from schemas import (
    PersonSchema,
    OfficialSchema,
    VehicleSchema,
    PERSON_COLLECTION,
    OFFICIAL_COLLECTION,
    VEHICLE_COLLECTION,
)


### Officials

def validate_official_exists(official: OfficialSchema):
    """Validate official exists in db, Return True if exists, False if is not"""
    official_col = mongodb.mydb[OFFICIAL_COLLECTION]
    return official_col.find_one({"number": official.number}) is not None


async def list_officials(skip: int = 0, limit: int = 10):
    """Returns list of officials"""
    officials_col = mongodb.mydb[OFFICIAL_COLLECTION]
    officials_list = officials_col.find({}).sort('timestamp', pymongo.DESCENDING
                                      ).skip(skip).limit(limit)
    return {"officials": list(officials_list)}


async def save_official(official: OfficialSchema):
    """New official in db"""
    if validate_official_exists(official):
        raise exceptions.ConflictException(f"Official {official.name} already exists")

    officials_col = mongodb.mydb[OFFICIAL_COLLECTION]
    new_official = officials_col.insert_one(dict(official))
    return new_official


async def drop_official(official: OfficialSchema):
    """drop official in db"""
    if not validate_official_exists(official):
        raise exceptions.NotFoundException(f"Official {official.name} not found")

    officials_col = mongodb.mydb[OFFICIAL_COLLECTION]
    officials_col.delete_one({"name": official.name, "number": official.number})


### Person

def validate_person_exists(person: PersonSchema):
    """Validate person exists in db, Return True if exists, False if is not"""
    person_col = mongodb.mydb[PERSON_COLLECTION]
    return person_col.find_one({"email": person.email}) is not None


async def list_persons(skip: int = 0, limit: int = 10):
    """Returns list of persons"""
    persons_col = mongodb.mydb[PERSON_COLLECTION]
    persons_list = persons_col.find({}).sort('name', pymongo.DESCENDING
                                      ).skip(skip).limit(limit)
    return {"persons": list(persons_list)}


async def save_person(person: PersonSchema):
    """Create a new person in db"""
    if validate_person_exists(person):
        raise exceptions.ConflictException(f"Person {person.name} already exists")

    persons_col = mongodb.mydb[OFFICIAL_COLLECTION]
    new_person = persons_col.insert_one(dict(person))
    return new_person


async def drop_person(person: PersonSchema):
    """drop person in db"""
    if not validate_person_exists(person):
        raise exceptions.NotFoundException(f"Person {person.name} not found")

    persons_col = mongodb.mydb[OFFICIAL_COLLECTION]
    persons_col.delete_one({"name": person.name, "email": person.email})


### Vehicle

def validate_vehicle_exists(vehicle: VehicleSchema):
    """Validate vehicle exists in db, Return True if exists, False if is not"""
    vehicle_col = mongodb.mydb[VEHICLE_COLLECTION]
    return vehicle_col.find_one({"plate_number": vehicle.plate_number}) is not None


async def list_vehicles(skip: int = 0, limit: int = 10):
    """Returns list of vehicles"""
    vehicles_col = mongodb.mydb[VEHICLE_COLLECTION]
    vehicles_list = vehicles_col.find({}).sort('plate_number', pymongo.DESCENDING
                                      ).skip(skip).limit(limit)
    return {"persons": list(vehicles_list)}


async def save_vehicle(vehicle: VehicleSchema):
    """Create a new vehicle in db"""
    if validate_vehicle_exists(vehicle):
        raise exceptions.ConflictException(f"Vehicle {vehicle.plate_number} already exists")

    vehicles_col = mongodb.mydb[VEHICLE_COLLECTION]
    new_vehicle = vehicles_col.insert_one(dict(vehicle))
    return new_vehicle


async def drop_vehicle(vehicle: VehicleSchema):
    """drop vehicle in db"""
    if not validate_vehicle_exists(vehicle):
        raise exceptions.NotFoundException(f"Vehicle {vehicle.plate_number} not found")

    vehicles_col = mongodb.mydb[VEHICLE_COLLECTION]
    vehicles_col.delete_one({"plate_number": vehicle.plate_number})
