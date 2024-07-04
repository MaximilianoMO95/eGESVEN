from typing import Optional
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.models.user import Role, Account
from app.schemas.user import RoleCreate, AccountCreate
from app.crud import user_crud, role_crud
from . import helpers


def create_random_role(db: Session) -> Role:
    name = helpers.random_lower_str()
    return role_crud.create(db, RoleCreate(name=name))


def create_random_user_account(db: Session, role_id: Optional[int] = None) -> Account:
    _ = role_id
    email = f"{helpers.random_lower_str()}@test.com"
    hashed_password = "fake_hash" + helpers.random_lower_str()

    user = AccountCreate(email=email, password=hashed_password)
    return user_crud.create_account(db, user)


def empty_user_records(db: Session) -> None:
    db.execute(delete(Account))
    db.commit()
