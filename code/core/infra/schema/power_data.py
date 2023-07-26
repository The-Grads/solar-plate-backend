from pydantic import BaseModel

from shared.infra.schema import Entity


class PowerData(Entity):
    solar_plate_id: str
    power_delivery: float


class CreatePowerData(BaseModel):
    solar_plate_id: str
    power_delivery: float

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "solar_plate_id": "2ea3c421-db0d-4feb-8d5d-e61b1da565b4",
                    "power_delivery": 10.1,
                }
            ]
        }
