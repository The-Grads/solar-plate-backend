from datetime import datetime
from typing import Annotated, List, Union

from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from core.infra.builder.user_builder import UserBuilder
from core.infra.factory.auth_service_factory import AuthServiceFactory
from core.infra.schema.user import CreateUser, User, UserToken

auth_router = APIRouter(
    tags=["auth"],
    prefix="/auth",
    responses={404: {"description": "Not found"}},
)
auth_service = AuthServiceFactory().create()


@auth_router.post("/", response_model=UserToken)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return auth_service.login(email=form_data.username, password=form_data.password)
