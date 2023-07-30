from typing import Dict, List

from sqlalchemy.orm.exc import NoResultFound

from core.domain.entity.solar_plate import SolarPlate
from core.domain.repository.solar_plate_repository import SolarPlateRepository
from core.infra.builder.solar_plate_builder import SolarPlateBuilder
from core.infra.models import SolarPlateModel
from setup.db import DBConnectionHandler


class DbSolarPlateRepository(SolarPlateRepository):
    builder: SolarPlateBuilder = SolarPlateBuilder()

    def find(self, id: str) -> SolarPlate:
        try:
            with DBConnectionHandler() as db:
                solar_plate = db.session.query(SolarPlateModel).filter_by(id=id).one()
                return self.builder.build_from_model(model=solar_plate)
        except NoResultFound:
            return None
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def find_all(self, filter: Dict = None) -> List[SolarPlate]:
        with DBConnectionHandler() as db:
            try:
                solar_plates = db.session.query(SolarPlateModel).all()
                return [
                    self.builder.build_from_model(model=solar_plate)
                    for solar_plate in solar_plates
                ]
            except Exception as exception:
                db.session.rollback()
                raise exception
            finally:
                db.session.close()

    def create(self, solar_plate: SolarPlate) -> List[SolarPlate]:
        with DBConnectionHandler() as db:
            try:
                solar_plate_model = SolarPlateModel(
                    name=solar_plate.name,
                    user_id=solar_plate.user_id,
                )
                db.session.add(solar_plate_model)
                db.session.commit()

                return self.builder.build_from_model(model=solar_plate_model)
            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None

    def update(self, solar_plate: SolarPlate) -> List[SolarPlate]:
        with DBConnectionHandler() as db:
            try:
                solar_plate_model = (
                    db.session.query(SolarPlateModel).filter_by(id=solar_plate.id).one()
                )
                solar_plate_model.name = solar_plate.name
                solar_plate_model.user_id = solar_plate.user_id

                db.session.add(solar_plate_model)
                db.session.commit()

                return self.builder.build_from_model(model=solar_plate_model)
            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None

    def delete(self, id: str) -> None:
        with DBConnectionHandler() as db:
            try:
                solar_plate_model = (
                    db.session.query(SolarPlateModel).filter_by(id=id).one()
                )
                db.session.delete(solar_plate_model)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None
