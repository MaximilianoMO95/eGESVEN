from sqlalchemy import Boolean, Integer, String
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.orm import relationship

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
    user_accounts = relationship("UserAccount", back_populates="role")
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")


class UserAccount(Base):
    __tablename__ = "user_accounts"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(80), nullable=False)
    is_active = Column(Boolean, default=True)

    # Foreign Keys
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    # Relationships
    role = relationship("Role", back_populates="user_accounts")
    profile = relationship("UserProfile", back_populates="user_account", uselist=False)
    client = relationship("Client", back_populates="user_account", uselist=False)


class UserProfile(Base):
    __tablename__ = "user_profiles"

    user_account_id = Column(Integer, ForeignKey("user_accounts.id"), primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    phone_number = Column(String(18), nullable=True)

    # Relationships
    user_account = relationship("UserAccount", back_populates="profile")


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    user_account_id = Column(Integer, ForeignKey("user_accounts.id"), unique=True, nullable=False)

    # Relationships
    user_account = relationship("UserAccount", back_populates="client")
    basket = relationship("Basket", back_populates="client")
