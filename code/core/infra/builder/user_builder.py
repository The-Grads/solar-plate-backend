from core.domain.entity import User
from core.infra.models.user import UserModel
from shared.infra.builder.base_builder import BaseBuilder

from .solar_plate_builder import SolarPlateBuilder


class UserBuilder(BaseBuilder):
    solar_plate_builder: SolarPlateBuilder = SolarPlateBuilder()

    def build(self, json_data: dict) -> User:
        return User(
            name=json_data.get("name"),
            email=json_data.get("email"),
            password=json_data.get("password"),
        )

    def build_from_model(self, model: UserModel):
        return User(
            id=str(model.id),
            name=model.name,
            email=model.email,
            password=model.password,
            solar_plates=[
                self.solar_plate_builder.build_from_model(model=solar_plate)
                for solar_plate in model.solar_plates
            ],
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
            archived_at=model.archived_at,
        )
