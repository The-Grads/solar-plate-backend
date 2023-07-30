from abc import ABC, abstractmethod
from typing import Dict, List

from core.domain.entity.company import Company


class CompanyRepository(ABC):
    @abstractmethod
    def find(self, id: str) -> Company:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, filter: Dict = {}) -> List[Company]:
        raise NotImplementedError

    @abstractmethod
    def create(self, Company: Company) -> List[Company]:
        raise NotImplementedError

    @abstractmethod
    def update(self, Company: Company) -> List[Company]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
