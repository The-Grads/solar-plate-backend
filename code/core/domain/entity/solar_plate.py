import dataclasses
from typing import List, Optional

from shared.domain.entity import BaseEntity

from .power_data import PowerData


@dataclasses.dataclass(init=True, frozen=True, slots=True, kw_only=True)
class SolarPlate(BaseEntity):
    user_id: str
    name: Optional[str] = None
    power_data: Optional[List[PowerData]] = None
