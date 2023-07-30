from core.domain.entity.company import Company
from core.infra.models.company import CompanyModel
from shared.infra.builder.base_builder import BaseBuilder


class CompanyBuilder(BaseBuilder):
    def build(self, json_data: dict) -> Company:
        return Company(
            name=json_data.get("name"),
        )

    def build_from_model(self, model: CompanyModel):
        return Company(
            id=str(model.id),
            name=str(model.name),
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
            archived_at=model.archived_at,
        )
