import datetime
from goat_database.models.meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
    )


class Goat(Base):
    __tablename__ = 'goat'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    mother_id = Column(Integer, nullable=True)
    father_id = Column(Integer, nullable=True)
    gender_id = Column(Integer, nullable=True)
    date_of_birth = Column(DateTime, nullable=False)
    breed_id = Column(Integer, nullable=False)
    birth_place = Column(UnicodeText, nullable=True)
