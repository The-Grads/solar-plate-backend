from typing import Dict, List

from sqlalchemy.orm.exc import NoResultFound

from core.domain.entity.power_data import PowerData
from core.domain.repository.power_data_repository import PowerDataRepository
from core.infra.builder.power_data_builder import PowerDataBuilder
from core.infra.models import PowerDataModel
from setup.db import DBConnectionHandler


class DbPowerDataRepository(PowerDataRepository):
    builder: PowerDataBuilder = PowerDataBuilder()

    def find(self, id: str) -> PowerData:
        try:
            with DBConnectionHandler() as db:
                power_data = db.session.query(PowerDataModel).filter_by(id=id).one()
                return self.builder.build_from_model(model=power_data)
        except NoResultFound:
            return None
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def find_all(self, filter: Dict = None) -> List[PowerData]:
        with DBConnectionHandler() as db:
            try:
                power_data_list = db.session.query(PowerDataModel).all()
                return [
                    self.builder.build_from_model(model=power_data)
                    for power_data in power_data_list
                ]
            except Exception as exception:
                db.session.rollback()
                raise exception
            finally:
                db.session.close()

    def create(self, power_data: PowerData) -> List[PowerData]:
        with DBConnectionHandler() as db:
            try:
                power_data_model = PowerDataModel(
                    power_delivery_ac=power_data.power_delivery_ac,
                    power_delivery_dc=power_data.power_delivery_dc,
                    solar_plate_id=power_data.solar_plate_id,
                    event_date=power_data.event_date,
                )
                db.session.add(power_data_model)
                db.session.commit()

                return self.builder.build_from_model(model=power_data_model)
            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None

    def update(self, power_data: PowerData) -> List[PowerData]:
        with DBConnectionHandler() as db:
            try:
                power_data_model = (
                    db.session.query(PowerDataModel).filter_by(id=power_data.id).one()
                )
                power_data_model.power_delivery_ac = power_data.power_delivery_ac
                power_data_model.power_delivery_dc = power_data.power_delivery_dc
                power_data_model.solar_plate_id = power_data.solar_plate_id
                power_data_model.event_date = power_data.event_date

                db.session.add(power_data_model)
                db.session.commit()

                return self.builder.build_from_model(model=power_data_model)
            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None

    def delete(self, id: str) -> None:
        with DBConnectionHandler() as db:
            try:
                power_data_model = (
                    db.session.query(PowerDataModel).filter_by(id=id).one()
                )
                db.session.delete(power_data_model)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None
