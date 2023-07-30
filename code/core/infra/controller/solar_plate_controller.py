from datetime import datetime
from typing import List

from fastapi import APIRouter

from core.infra.builder.solar_plate_builder import SolarPlateBuilder
from core.infra.factory.solar_service_plate_factory import SolarPlateServiceFactory
from core.infra.schema.solar_plate import CreateSolarPlate, SolarPlate

solar_plate_router = APIRouter(
    tags=["Solar Plate"],
    prefix="/solar_plate",
    responses={404: {"description": "Not found"}},
)
solar_plate_service = SolarPlateServiceFactory().create()


@solar_plate_router.get("/", response_model=List[SolarPlate])
async def list_solar_plate():
    return solar_plate_service.solar_plate_repository.find_all()


@solar_plate_router.get("/{id}", response_model=SolarPlate)
async def get_solar_plate(id: str):
    return solar_plate_service.solar_plate_repository.find(id=id)


@solar_plate_router.post("/", response_model=SolarPlate)
async def create_solar_plate(solar_plate: CreateSolarPlate):
    solar_plate_builder = SolarPlateBuilder()
    created_solar_plate = solar_plate_service.create(
        solar_plate=solar_plate_builder.build(dict(solar_plate)),
    )
    return created_solar_plate
