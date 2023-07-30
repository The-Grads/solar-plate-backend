from typing import List

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, relationship

from shared.infra.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = Column(String(50))
    email: Mapped[str] = Column(String(50), nullable=False, unique=True)
    password: Mapped[str] = Column(String, nullable=False)
    company_id: Mapped[int] = Column(UUID(as_uuid=True), ForeignKey("company.id"))
    company: Mapped["CompanyModel"] = relationship(
        "CompanyModel", back_populates="users"
    )
    solar_plates: Mapped[List["SolarPlateModel"]] = relationship(
        "SolarPlateModel", back_populates="user", cascade="all, delete"
    )
