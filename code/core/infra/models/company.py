from typing import List

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from shared.infra.models import BaseModel


class CompanyModel(BaseModel):
    __tablename__ = "company"

    name: Mapped[str] = Column(
        String(50),
        nullable=False,
    )
    users: Mapped[List["UserModel"]] = relationship(
        "UserModel", back_populates="company", cascade="all, delete"
    )
