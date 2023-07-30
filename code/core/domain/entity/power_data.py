import dataclasses
from datetime import datetime
from typing import Optional

from shared.domain.entity import BaseEntity


@dataclasses.dataclass(init=True, frozen=True, slots=True, kw_only=True)
class PowerData(BaseEntity):
    solar_plate_id: str
    power_delivery: float
    event_date: Optional[datetime] = None
