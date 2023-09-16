from sqlalchemy import text

from setup.db import DBConnectionHandler


class LoadInitalData:
    def run(self):
        try:
            with DBConnectionHandler() as db:
                with open(
                    "/home/python/app/code/core/infra/script/sql/initial_data.sql"
                ) as file:
                    query = text(file.read())
                    db.session.execute(query)
                    db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()


LoadInitalData().run()
