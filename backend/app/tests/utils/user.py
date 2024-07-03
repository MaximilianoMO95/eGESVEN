from typing import Optional
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.models.user import Role, UserAccount
from app.schemas.user import RoleCreate, UserCreate
from app.crud.user import UserCrud as crud_user
from app.crud.user import RoleCrud as crud_role
from . import helpers


def create_random_role(db: Session) -> Role:
    name = helpers.random_lower_str()
    return crud_role.create_role(db, RoleCreate(name=name))


def create_random_user(db: Session, role_id: Optional[int] = None) -> UserAccount:
    _ = role_id
    email = f"{helpers.random_lower_str()}@test.com"
    hashed_password = "fake_hash" + helpers.random_lower_str()

    user = UserCreate(email=email, password=hashed_password)
    return crud_user.create_user(db, user)


def empty_user_records(db: Session) -> None:
    db.execute(delete(UserAccount))
    db.commit()
