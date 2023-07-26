import uuid
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Optional



@dataclass(init=True, frozen=True, slots=True, kw_only=True)
class BaseEntity:
    id: str | None = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None

    def to_dict(self):
        return asdict(self)

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def __str__(self) -> str:
        return f"{self.id}"
