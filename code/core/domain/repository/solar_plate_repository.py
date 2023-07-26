from abc import ABC, abstractmethod
from typing import Dict, List

from core.domain.entity.solar_plate import SolarPlate


class SolarPlateRepository(ABC):
    @abstractmethod
    def find(self, id: str) -> SolarPlate:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, filter: Dict) -> List[SolarPlate]:
        raise NotImplementedError

    @abstractmethod
    def create(self, solar_plate: SolarPlate) -> List[SolarPlate]:
        raise NotImplementedError

    @abstractmethod
    def update(self, solar_plate: SolarPlate) -> List[SolarPlate]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
