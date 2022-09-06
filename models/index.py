from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String((255)))
    pets = relationship('Pet', back_populates='owner')


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    price = Column(Float)
    animal_type = Column(String(255))
    description = Column(Text)
    is_active = Column(Boolean)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='pets')
