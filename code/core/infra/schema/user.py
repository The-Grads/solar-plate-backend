from typing import List, Optional

from pydantic import BaseModel

from shared.infra.schema import Entity

from .solar_plate import SolarPlate


class User(Entity):
    name: str
    email: str | None = None
    solar_plates: Optional[List[SolarPlate]]


class UserToken(BaseModel):
    access_token: str
    token_type: str


class CreateUser(BaseModel):
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
