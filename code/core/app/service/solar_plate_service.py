from core.domain.entity.solar_plate import SolarPlate
from core.domain.repository.solar_plate_repository import SolarPlateRepository


class SolarPlateService:
    def __init__(self, solar_plate_repository: SolarPlateRepository) -> None:
        self.__solar_plate_repository = solar_plate_repository

    @property
    def solar_plate_repository(self) -> SolarPlateRepository:
        return self.__solar_plate_repository

    def create(self, solar_plate: SolarPlate) -> SolarPlate:
        return self.__solar_plate_repository.create(solar_plate=solar_plate)

    def update(self, solar_plate: SolarPlate) -> SolarPlate:
        return self.__solar_plate_repository.update(solar_plate=solar_plate)

    def delete(self, id: int) -> SolarPlate:
        self.__solar_plate_repository.delete(id=id)
