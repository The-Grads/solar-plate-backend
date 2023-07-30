from core.app.service.company_service import CompanyService
from core.infra.repository.db_company_repository import DbCompanyRepository


class CompanyServiceFactory:
    def create(self) -> CompanyService:
        return CompanyService(company_repository=DbCompanyRepository())
