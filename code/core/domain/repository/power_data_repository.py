from abc import ABC, abstractmethod
from typing import Dict, List

from core.domain.entity.power_data import PowerData


class PowerDataRepository(ABC):
    @abstractmethod
    def find(self, id: str) -> PowerData:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, filter: Dict) -> List[PowerData]:
        raise NotImplementedError

    @abstractmethod
    def create(self, power_data: PowerData) -> List[PowerData]:
        raise NotImplementedError

    @abstractmethod
    def update(self, power_data: PowerData) -> List[PowerData]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
