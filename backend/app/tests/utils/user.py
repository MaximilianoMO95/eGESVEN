from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import Role, User
from app.schemas.user import UserCreate
from app.crud.user import UserCrud as crud_user
from app.crud.user import RoleCrud as crud_role
from . import utils


def create_random_role(db: Session) -> Role:
    name = utils.random_lower_str()
    return crud_role.create_role(db, name)


def create_random_user(db: Session, role_id: Optional[int] = None) -> User:
    _ = role_id
    email = f"{utils.random_lower_str()}@test.com"
    hashed_password = "fake_hash" + utils.random_lower_str()

    user = UserCreate(email=email, password=hashed_password)
    return crud_user.create_user(db, user)
