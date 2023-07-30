from core.app.service.solar_plate_service import SolarPlateService
from core.infra.repository.db_solar_plate_repository import DbSolarPlateRepository


class SolarPlateServiceFactory:
    def create(self) -> SolarPlateService:
        return SolarPlateService(solar_plate_repository=DbSolarPlateRepository())
