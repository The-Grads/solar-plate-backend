from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from shared.infra.schema import Entity


class PowerData(Entity):
    solar_plate_id: str
    power_delivery_ac: Optional[float]
    power_delivery_dc: Optional[float]
    event_date: Optional[datetime]


class UpdatePowerData(BaseModel):
    power_delivery_ac: Optional[float]
    power_delivery_dc: Optional[float]
    event_date: Optional[datetime]

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "power_delivery_ac": 10.1,
                    "power_delivery_dc": 10.1,
                    "event_date": "2023-07-20T14:12:37.723919",
                }
            ]
        }


class CreatePowerData(BaseModel):
    solar_plate_id: str
    power_delivery_ac: Optional[float]
    power_delivery_dc: Optional[float]
    event_date: Optional[datetime]

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "solar_plate_id": "2ea3c421-db0d-4feb-8d5d-e61b1da565b4",
                    "power_delivery_ac": 10.1,
                    "power_delivery_dc": 10.1,
                    "event_date": "2023-07-20T14:12:37.723919",
                }
            ]
        }
