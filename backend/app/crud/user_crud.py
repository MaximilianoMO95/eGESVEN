from sqlalchemy.orm import Session

from typing import List, Set, cast

from app.schemas.user import  ProfileCreate, RoleCreate, AccountCreate
from app.models.user import Account, Permission, Profile
from . import role_crud


def get_account(db: Session, user_id: int) -> Account|None:
    return db.query(Account).filter(Account.id == user_id).first()


def get_account_by_email(db: Session, email: str) -> Account|None:
    return db.query(Account).filter(Account.email == email).first()


def get_account_list(db: Session, skip: int = 0, limit: int = 10) -> List[Account]|None:
    return db.query(Account).offset(skip).limit(limit).all()


def create_account(db: Session, user: AccountCreate) -> Account:
    # TODO: Implement password hashing (SHA256)
    fake_hashed_password = user.password + "notreallyhashed"

    role = role_crud.get_by_name(db, "client");
    if not role:
        role = role_crud.create(db, RoleCreate(name="client"));

    db_user = Account(email=user.email, hashed_password=fake_hashed_password, role_id=role.id)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(**profile.model_dump())

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    return db_profile


def get_permissions(db: Session, user_id: int) -> Set[Permission]|None:
    user = db.query(Account).filter(Account.id == user_id).first()
    if not user:
        return None


    role = role_crud.get(db, cast(int, user.role_id))
    if not role:
        return None

    permissions = set()
    for perm in role.permissions:
        permissions.add(perm.name)

    return permissions


def have_permission(db: Session, user_id: int, permission: str) -> bool:
    permissions = get_permissions(db, user_id)
    if not permissions or permission not in permissions:
        return False

    return True
