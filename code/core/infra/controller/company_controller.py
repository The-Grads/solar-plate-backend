from datetime import datetime
from typing import List

from fastapi import APIRouter

from core.infra.builder.company_builder import CompanyBuilder
from core.infra.factory.company_service_factory import CompanyServiceFactory
from core.infra.schema.company import Company, CreateCompany, UpdateCompany

company_router = APIRouter(
    tags=["Company"],
    prefix="/company",
    responses={404: {"description": "Not found"}},
)
company_service = CompanyServiceFactory().create()


@company_router.get("/", response_model=List[Company])
async def list_company():
    return company_service.company_repository.find_all()


@company_router.get("/{id}", response_model=Company)
async def get_company(id: str):
    return company_service.company_repository.find(id=id)


@company_router.post("/", response_model=Company)
async def create_company(company: CreateCompany):
    company_builder = CompanyBuilder()
    created_company = company_service.create(
        company=company_builder.build(dict(company)),
    )
    return created_company


@company_router.put("/{id}", response_model=Company)
async def update_power_data(id: str, power_data: UpdateCompany):
    company_builder = CompanyBuilder()
    company = company_service.update(
        company=company_builder.build({"id": id, **dict(power_data)}),
    )
    return company


@company_router.delete("/{id}")
async def update_power_data(id: str):
    company_service.delete(id)
