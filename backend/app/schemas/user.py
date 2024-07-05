from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel
from pydantic.config import ConfigDict

from app.schemas.basket import BasketPublic


# User Permissions
class PermissionBase(BaseModel):
    name: str
    description: str | None = None


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(PermissionBase):
    pass


class Permission(PermissionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# User Roles
class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# User Accounts
class AccountBase(BaseModel):
    email: str


class AccountCreate(AccountBase):
    password: str


class AccountPublic(AccountBase):
    id: int
    user_id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


# User Profiles
class ProfileBase(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    date_of_birth: datetime


class ProfileCreate(ProfileBase):
    pass


class ProfilePublic(ProfileBase):

    model_config = ConfigDict(from_attributes=True)


# Users
class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    role_id: Optional[int] = None


class UserPublic(UserBase):
    id: int
    role_id: int

    model_config = ConfigDict(from_attributes=True)


# Clients
class ClientBase(BaseModel):
    user_id: int


class ClientCreate(ClientBase):
    pass


class ClientPublic(ClientBase):
    id: int
    basket: BasketPublic

    model_config = ConfigDict(from_attributes=True)


# Token
class TokenCreate(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: int | None = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: Optional[str] = None
    expires_at: Optional[timedelta] = None
