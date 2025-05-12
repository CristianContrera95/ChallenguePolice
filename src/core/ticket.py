import pymongo
from click import open_file
from pyasn1.type.univ import Boolean
from pydantic import EmailStr

import core.exceptions as exceptions
from api import mongodb
from core.entities_crud import validate_vehicle_exists
from schemas import (
    TicketSchema,
    TicketResponseSchema,
    OfficialSchema,
    TICKET_COLLECTION,
    OFFICIAL_COLLECTION,
    PERSON_COLLECTION,
    VEHICLE_COLLECTION
)


def validate_official_exists(official: OfficialSchema):
    """Validate official exists in db, Return True if exists, False if is not"""
    official_col = mongodb.mydb[OFFICIAL_COLLECTION]
    official = official_col.find_one({"name": official.name, "number": official.number})
    return official is not None


def validate_plate_exists(plate: str):
    """Validate a license plate exists in db, Return True if it exists, False if is not"""
    vehicle_col = mongodb.mydb[VEHICLE_COLLECTION]
    vehicle = vehicle_col.find_one({"plate_number": plate})
    return vehicle is not None


def validate_person_exists(email: EmailStr):
    """Validate a license plate exists in db, Return True if it exists, False if is not"""
    person_col = mongodb.mydb[PERSON_COLLECTION]
    person = person_col.find_one({"email": email})
    return person is not None


async def get_tickets_by_email(email: EmailStr, skip: int = 0, limit: int = 10):
    """Returns list of tickets"""
    ticket_col = mongodb.mydb[TICKET_COLLECTION]
    ticket_list = ticket_col.find({"person_email": email}).sort('timestamp', pymongo.DESCENDING
                                      ).skip(skip).limit(limit)
    ticket_list = [TicketResponseSchema(**t) for t in ticket_list]
    return ticket_list


async def save_ticket(new_ticket: TicketSchema, official: OfficialSchema):
    """Create a new ticket in db"""

    # Validate data
    if validate_official_exists(official):
        if validate_plate_exists(new_ticket.license_plate):
            if validate_person_exists(new_ticket.person_email):
                # add a new person with email as name
                person_col = mongodb.mydb[PERSON_COLLECTION]
                name = str(new_ticket.person_email).split('.')[0]
                person_col.insert_one({"name": name, "email": new_ticket.person_email})
            new_ticket = dict(new_ticket)
            tickets = mongodb.mydb[TICKET_COLLECTION]

            # Save model
            new_ticket = tickets.insert_one(new_ticket)
        else:
            raise exceptions.PlateNotFoundException(f"License plate {new_ticket.license_plate} is not valid")
    else:
        raise exceptions.NoAccessException(f"Official {official.name} not exists")
    return new_ticket

