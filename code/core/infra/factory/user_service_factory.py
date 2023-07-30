from core.app.service import UserService
from core.infra.repository import DbUserRepository


class UserServiceFactory:
    def create(self) -> UserService:
        return UserService(user_repository=DbUserRepository())
