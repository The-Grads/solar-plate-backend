import dataclasses
from typing import List, Optional

from passlib.context import CryptContext

from shared.domain.entity import BaseEntity

from .solar_plate import SolarPlate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@dataclasses.dataclass(init=True, frozen=True, slots=True, kw_only=True)
class User(BaseEntity):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    solar_plates: Optional[List[SolarPlate]] = None

    def set_password(self, password: str) -> None:
        self._set("password", pwd_context.hash(password.encode("utf-8")))
