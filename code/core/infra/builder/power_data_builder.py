from core.domain.entity.power_data import PowerData
from core.infra.models.power_data import PowerDataModel
from shared.infra.builder.base_builder import BaseBuilder


class PowerDataBuilder(BaseBuilder):
    def build(self, json_data: dict) -> PowerData:
        return PowerData(
            id=json_data.get("id"),
            solar_plate_id=json_data.get("solar_plate_id"),
            power_delivery=json_data.get("power_delivery"),
            event_date=json_data.get("event_date"),
        )

    def build_from_model(self, model: PowerDataModel):
        return PowerData(
            id=str(model.id),
            solar_plate_id=str(model.solar_plate_id),
            power_delivery=model.power_delivery,
            event_date=model.event_date,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
            archived_at=model.archived_at,
        )
