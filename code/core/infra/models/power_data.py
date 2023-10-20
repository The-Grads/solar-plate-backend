from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, relationship

from shared.infra.models import BaseModel


class PowerDataModel(BaseModel):
    __tablename__ = "power_data"

    power_delivery_ac: float = Column(
        Float,
        nullable=True,
    )
    power_delivery_dc: float = Column(
        Float,
        nullable=True,
    )
    event_date: Mapped[datetime] = Column(DateTime, nullable=True)
    solar_plate_id: Mapped[int] = Column(
        UUID(as_uuid=True), ForeignKey("solar_plate.id")
    )
    solar_plate: Mapped["SolarPlateModel"] = relationship(
        "SolarPlateModel", back_populates="power_data"
    )
