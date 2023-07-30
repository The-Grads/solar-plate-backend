from typing import Dict, List

from sqlalchemy.orm.exc import NoResultFound

from core.domain.entity import User
from core.domain.repository import UserRepository
from core.infra.builder.user_builder import UserBuilder
from core.infra.models import UserModel
from setup.db import DBConnectionHandler


class DbUserRepository(UserRepository):
    builder: UserBuilder = UserBuilder()

    def find(self, id: str) -> User:
        try:
            with DBConnectionHandler() as db:
                user = db.session.query(UserModel).filter_by(id=id).one()
                return self.builder.build_from_model(model=user)
        except NoResultFound:
            return None
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def find_by_email(self, email: str) -> User:
        try:
            with DBConnectionHandler() as db:
                user = db.session.query(UserModel).filter_by(email=email).one()
                return self.builder.build_from_model(model=user)
        except NoResultFound:
            return None
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def find_all(self, filter: Dict = None) -> List[User]:
        with DBConnectionHandler() as db:
            try:
                users = db.session.query(UserModel).all()
                return [self.builder.build_from_model(model=user) for user in users]
            except Exception as exception:
                db.session.rollback()
                raise exception
            finally:
                db.session.close()

    def create(self, user: User) -> List[User]:
        with DBConnectionHandler() as db:
            try:
                user_model = UserModel(
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    company_id=user.company_id,
                )
                db.session.add(user_model)
                db.session.commit()

                return self.builder.build_from_model(model=user_model)
            except Exception as error:
                db.session.rollback()
                raise error
            finally:
                db.session.close()

        return None

    def update(self, user: User) -> List[User]:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
