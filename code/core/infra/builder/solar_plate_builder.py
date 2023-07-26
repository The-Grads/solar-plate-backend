from core.domain.entity.solar_plate import SolarPlate
from core.infra.models.solar_plate import SolarPlateModel
from shared.infra.builder.base_builder import BaseBuilder

from .power_data_builder import PowerDataBuilder


class SolarPlateBuilder(BaseBuilder):
    power_data_builder: PowerDataBuilder = PowerDataBuilder()

    def build(self, json_data: dict) -> SolarPlate:
        return SolarPlate(
            name=json_data.get("name"),
            user_id=json_data.get("user_id"),
        )

    def build_from_model(self, model: SolarPlateModel):
        return SolarPlate(
            id=str(model.id),
            name=model.name,
            user_id=str(model.user_id),
            power_data=[
                self.power_data_builder.build_from_model(model=power_data)
                for power_data in model.power_data
            ],
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
            archived_at=model.archived_at,
        )
