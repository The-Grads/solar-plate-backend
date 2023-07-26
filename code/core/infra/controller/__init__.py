from fastapi import APIRouter

from .power_data_controller import power_data_router
from .solar_plate_controller import solar_plate_router
from .user_controller import user_router

core_router = APIRouter(
    prefix="/core",
    responses={404: {"description": "Not found"}},
)

core_router.include_router(user_router)
core_router.include_router(solar_plate_router)
core_router.include_router(power_data_router)
