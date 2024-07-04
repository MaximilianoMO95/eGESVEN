from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.db import Base


# Association tables
role_permissions = Table(
    "role_permissions", Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permissions.id"), primary_key=True)
)


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(254), nullable=True)

    # Relationships
    roles = relationship("Role", secondary=role_permissions, back_populates="permissions")


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, nullable=False)

    # Relationships
    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(80), nullable=False)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="account")


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    phone_number = Column(String(18), nullable=True)

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="profile")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Foreign Keys
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    # Relationships
    role = relationship("Role", back_populates="users")
    account = relationship("Account", back_populates="user", uselist=False)
    profile = relationship("Profile", back_populates="user", uselist=False)
    client = relationship("Client", back_populates="user", uselist=False)


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    # Relationships
    user = relationship("User", back_populates="client")
    basket = relationship("Basket", back_populates="client")
