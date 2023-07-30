from core.app.service.auth_service import AuthService
from core.infra.repository import DbUserRepository


class AuthServiceFactory:
    def create(self) -> AuthService:
        return AuthService(user_repository=DbUserRepository())
