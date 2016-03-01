from goat_database.models.meta import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
    ForeignKey,
    )


class Breed(Base):
    __tablename__ = 'breed'
    breed_id = Column(Integer, primary_key=True)
    breed_name = Column(Unicode(255), nullable=False)
    goat = relationship("Goat", backref="breed")


class Gender(Base):
    __tablename__ = 'gender'
    gender_id = Column(Integer, primary_key=True)
    gender_name = Column(Unicode(255), nullable=False)
    goat = relationship("Goat", backref="gender")


class Goat(Base):
    __tablename__ = 'goat'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    mother_id = Column(Integer, nullable=True)
    father_id = Column(Integer, nullable=True)
    gender_id = Column(Integer, ForeignKey('gender.gender_id'), nullable=True)
    date_of_birth = Column(DateTime, nullable=False)
    breed_id = Column(Integer, ForeignKey('breed.breed_id'), nullable=False)
    birth_place = Column(UnicodeText, nullable=True)
