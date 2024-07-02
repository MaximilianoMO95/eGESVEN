from typing import Optional
from pydantic import BaseModel
from pydantic.config import ConfigDict

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


# User Role Table
class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# User Table
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserPublic(UserBase):
    id: int
    is_active: bool
    role: Role

    model_config = ConfigDict(from_attributes=True)


# Person Table
class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class ProfilePublic(ProfileBase):
    user: UserPublic

    model_config = ConfigDict(from_attributes=True)
