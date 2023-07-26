from typing import List

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from shared.infra.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = Column(String(50))
    email: Mapped[str] = Column(String(50), nullable=False, unique=True)
    password: Mapped[str] = Column(String, nullable=False)

    solar_plates: Mapped[List["SolarPlateModel"]] = relationship(
        "SolarPlateModel", back_populates="user", cascade="all, delete"
    )
