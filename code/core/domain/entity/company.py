import dataclasses
from typing import List, Optional

from shared.domain.entity import BaseEntity

from .user import User


@dataclasses.dataclass(init=True, frozen=True, slots=True, kw_only=True)
class Company(BaseEntity):
    name: Optional[str] = None
    users: Optional[List[User]]
