from abc import ABC, abstractmethod
from typing import Dict, List

from core.domain.entity import User


class UserRepository(ABC):
    @abstractmethod
    def find(self, id: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, filter: Dict = {}) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
