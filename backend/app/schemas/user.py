from typing import Optional
from pydantic import BaseModel
from pydantic.config import ConfigDict

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


class User(UserBase):
    id: int
    is_active: bool
    role: Role

    model_config = ConfigDict(from_attributes=True)


# Person Table
class PersonBase(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: Optional[str] = None


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    user: User

    model_config = ConfigDict(from_attributes=True)
