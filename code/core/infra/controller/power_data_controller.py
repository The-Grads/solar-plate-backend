from datetime import datetime
from typing import List

from fastapi import APIRouter

from core.infra.builder.power_data_builder import PowerDataBuilder
from core.infra.factory.power_data_factory import PowerDataServiceFactory
from core.infra.schema.power_data import CreatePowerData, PowerData

power_data_router = APIRouter(
    tags=["Power Data"],
    prefix="/power_data",
    responses={404: {"description": "Not found"}},
)
power_data_service = PowerDataServiceFactory().create()


@power_data_router.get("/", response_model=List[PowerData])
async def list_power_data():
    return power_data_service.power_data_repository.find_all()


@power_data_router.get("/{id}", response_model=PowerData)
async def get_power_data(id: str):
    return power_data_service.power_data_repository.find(id=id)


@power_data_router.post("/", response_model=PowerData)
async def create_power_data(power_data: CreatePowerData):
    power_data_builder = PowerDataBuilder()
    created_power_data = power_data_service.create(
        power_data=power_data_builder.build(dict(power_data)),
    )
    return created_power_data
