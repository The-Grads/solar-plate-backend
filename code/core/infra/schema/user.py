from typing import List, Optional

from pydantic import BaseModel

from shared.infra.schema import Entity

from .solar_plate import SolarPlate


class User(Entity):
    name: str
    company_id: Optional[str] = None
    email: str | None = None
    solar_plates: Optional[List[SolarPlate]]


class UserToken(BaseModel):
    user_id: str
    access_token: str
    token_type: str


class UpdateUser(BaseModel):
    name: str
    password: str
    email: str | None = None

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "User",
                    "email": "test@test.com",
                    "password": "password",
                }
            ]
        }


class CreateUser(BaseModel):
    name: str
    password: str
    company_id: Optional[str] = None
    email: str | None = None

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "User",
                    "email": "test@test.com",
                    "password": "password",
                    "company_id": "2b7211c7-59d2-4029-a725-906caab00272",
                }
            ]
        }
