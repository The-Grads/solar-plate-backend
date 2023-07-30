from datetime import datetime, timedelta

import bcrypt
from jose import JWTError, jwt
from passlib.context import CryptContext

from core.domain.repository.user_repository import UserRepository
from setup.config import Config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def login(self, email: str, password: str, expires_in: int = 24):
        user = self.__user_repository.find_by_email(email=email)

        if user is None:
            raise ValueError("Invalid username or password")

        if not pwd_context.verify(
            password.encode("utf-8"), user.password.encode("utf-8")
        ):
            raise ValueError("Invalid username or password")

        expired_at = datetime.utcnow() + timedelta(hours=expires_in)
        payload = {"sub": user.email, "exp": expired_at}
        access_token = jwt.encode(payload, Config.APP_SECRET_KEY)

        return {"access_token": access_token, "token_type": "bearer"}

    def verify_token(self, access_token):
        try:
            data = jwt.decode(access_token, Config.APP_SECRET_KEY)
        except JWTError:
            raise ValueError("Invalid username or password")

        user = self.__user_repository.find_by_email(email=data["sub"])

        if user is None:
            raise ValueError("Invalid username or password")

        return user
