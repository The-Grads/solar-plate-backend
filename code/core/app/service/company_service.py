from core.domain.entity.company import Company
from core.domain.repository.company_repository import CompanyRepository


class CompanyService:
    def __init__(self, company_repository: CompanyRepository) -> None:
        self.__company_repository = company_repository

    @property
    def company_repository(self) -> CompanyRepository:
        return self.__company_repository

    def create(self, company: Company) -> Company:
        return self.__company_repository.create(company=company)

    def update(self, company: Company) -> Company:
        return self.__company_repository.update(company=company)

    def delete(self, id: int) -> Company:
        self.__company_repository.delete(id=id)
