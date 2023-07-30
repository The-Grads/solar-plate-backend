from typing import List, Optional

from pydantic import BaseModel

from shared.infra.schema import Entity

from .power_data import PowerData


class SolarPlate(Entity):
    name: str
    user_id: str | None = None
    power_data: Optional[List[PowerData]]


class UpdateSolarPlate(BaseModel):
    name: str

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "SolarPlate",
                }
            ]
        }


class CreateSolarPlate(BaseModel):
    name: str
    user_id: str | None = None

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "SolarPlate",
                    "user_id": "2ea3c421-db0d-4feb-8d5d-e61b1da565b4",
                }
            ]
        }
