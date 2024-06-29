from sqlalchemy import Boolean, Integer, String
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, nullable=False)

    # Relationships
    users = relationship('User', back_populates='role')


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(80), nullable=False)
    is_active = Column(Boolean, default=True)

    role_id = Column(Integer, ForeignKey('roles.id'))

    # Relationships
    role = relationship('Role', back_populates='users')
    person = relationship('Person', back_populates='user', uselist=False)



class Person(Base):
    __tablename__ = "persons"

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    address = Column(String(160), nullable=False)
    phone_number = Column(String(18), nullable=True)

    # Relationships
    user = relationship('User', back_populates='person', uselist=False)
