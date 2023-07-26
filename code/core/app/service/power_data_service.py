from core.domain.entity.power_data import PowerData
from core.domain.repository.power_data_repository import PowerDataRepository


class PowerDataService:
    def __init__(self, power_data_repository: PowerDataRepository) -> None:
        self.__power_data_repository = power_data_repository

    @property
    def power_data_repository(self) -> PowerDataRepository:
        return self.__power_data_repository

    def create(self, power_data: PowerData) -> PowerData:
        return self.__power_data_repository.create(power_data=power_data)

    def update(self, power_data: PowerData) -> PowerData:
        return self.__power_data_repository.update(power_data=power_data)

    def delete(self, id: int) -> PowerData:
        self.__power_data_repository.delete(id=id)
