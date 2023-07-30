from typing import List, Optional

from pydantic import BaseModel

from shared.infra.schema import Entity

from .user import User


class Company(Entity):
    name: str
    users: Optional[List[User]]


class CreateCompany(BaseModel):
    name: str

    class Config:
        json_schema_extra = {"examples": [{"name": "Company"}]}
