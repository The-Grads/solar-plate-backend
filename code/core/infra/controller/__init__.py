from typing import Annotated, List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from core.infra.factory.auth_service_factory import AuthServiceFactory

from .auth_controller import auth_router
from .company_controller import company_router
from .power_data_controller import power_data_router
from .solar_plate_controller import solar_plate_router
from .user_controller import user_router

core_router = APIRouter(
    prefix="/core",
    responses={404: {"description": "Not found"}},
)
auth_service = AuthServiceFactory().create()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="core/auth")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    return auth_service.verify_token(access_token=token)


core_router.include_router(auth_router)
core_router.include_router(company_router, dependencies=[Depends(get_current_user)])
core_router.include_router(user_router, dependencies=[Depends(get_current_user)])
core_router.include_router(solar_plate_router, dependencies=[Depends(get_current_user)])
core_router.include_router(power_data_router, dependencies=[Depends(get_current_user)])
