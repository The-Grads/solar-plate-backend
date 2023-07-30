from typing import Dict, List

from sqlalchemy.orm.exc import NoResultFound

from core.domain.entity.company import Company
from core.domain.repository.company_repository import CompanyRepository
from core.infra.builder.company_builder import CompanyBuilder
from core.infra.models.company import CompanyModel
from setup.db import DBConnectionHandler


class DbCompanyRepository(CompanyRepository):
    builder: CompanyBuilder = CompanyBuilder()

    def find(self, id: str) -> Company:
        try:
            with DBConnectionHandler() as db:
                company = db.session.query(CompanyModel).filter_by(id=id).one()
                return self.builder.build_from_model(model=company)
        except NoResultFound:
            return None
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def find_all(self, filter: Dict = None) -> List[Company]:
        with DBConnectionHandler() as db:
            try:
                companys = db.session.query(CompanyModel).all()
                return [
                    self.builder.build_from_model(model=company) for company in companys
                ]
            except Exception as exception:
                db.session.rollback()
                raise exception
            finally:
                db.session.close()

    def create(self, company: Company) -> List[Company]:
        with DBConnectionHandler() as db:
            try:
                company_model = CompanyModel(name=company.name)
                db.session.add(company_model)
                db.session.commit()

                return self.builder.build_from_model(model=company_model)
            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None

    def update(self, company: Company) -> List[Company]:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
