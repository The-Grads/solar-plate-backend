import dataclasses
from typing import Optional

from shared.domain.entity import BaseEntity


@dataclasses.dataclass(init=True, frozen=True, slots=True, kw_only=True)
class PowerData(BaseEntity):
    solar_plate_id: int
    power_delivery: float
