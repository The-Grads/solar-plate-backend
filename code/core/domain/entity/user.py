import dataclasses
from typing import List, Optional

import bcrypt

from shared.domain.entity import BaseEntity

from .solar_plate import SolarPlate


@dataclasses.dataclass(init=True, frozen=True, slots=True, kw_only=True)
class User(BaseEntity):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    solar_plates: Optional[List[SolarPlate]] = None

    def set_password(self, password: str) -> None:
        self._set("password", bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()))
