from core.app.service.power_data_service import PowerDataService
from core.infra.repository.db_power_data_repository import DbPowerDataRepository


class PowerDataServiceFactory:
    def create(self) -> PowerDataService:
        return PowerDataService(power_data_repository=DbPowerDataRepository())
