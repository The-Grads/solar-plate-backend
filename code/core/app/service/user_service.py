from core.domain.entity import User
from core.domain.repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.__user_repository = user_repository

    @property
    def user_repository(self) -> UserRepository:
        return self.__user_repository

    def create(self, user: User) -> User:
        user.set_password(user.password)
        return self.__user_repository.create(user=user)

    def update(self, user: User) -> User:
        return self.__user_repository.update(user=user)

    def delete(self, id: int) -> User:
        self.__user_repository.delete(id=id)
