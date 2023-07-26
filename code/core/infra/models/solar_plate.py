from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, relationship

from shared.infra.models import BaseModel


class SolarPlateModel(BaseModel):
    __tablename__ = "solar_plate"

    name: Mapped[str] = Column(String(50))
    user_id: Mapped[int] = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="solar_plates")
    power_data: Mapped[List["PowerDataModel"]] = relationship(
        "PowerDataModel", back_populates="solar_plate", cascade="all, delete"
    )
