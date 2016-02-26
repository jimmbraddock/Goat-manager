import sqlalchemy as sa
from ..meta import DBSession
from ..goat import Goat


class GoatService:

    @classmethod
    def all(cls):
        return DBSession.query(Goat).order_by(sa.desc(Goat.date_of_birth))

    @classmethod
    def by_id(cls, id):
        return DBSession.query(Goat).filter(Goat.id == id).first()
