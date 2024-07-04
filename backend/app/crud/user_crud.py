from sqlalchemy.orm import Session
from typing import List, Optional, Set, cast

from app.core.security import get_password_hash, verify_password
from app.schemas.user import  ProfileCreate, RoleCreate, AccountCreate
from app.schemas.user import  UserCreate
from app.models.user import Account, Permission, Profile, User
from app.core.db import DEFAULT_ROLE_NAME

from . import role_crud


def _create_user(db: Session, user: UserCreate) -> User:
    role = role_crud.get_by_name(db, DEFAULT_ROLE_NAME);
    if not role:
        role = role_crud.create(db, RoleCreate(name=DEFAULT_ROLE_NAME));


    if user.role_id is None:
        user.role_id = cast(int, role.id)

    db_user = User(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, user_id: int) -> User|None:
    return db.query(User).filter(User.id == user_id).first()


def get_account(db: Session, user_id: int) -> Account|None:
    return db.query(Account).filter(Account.user_id == user_id).first()


def get_account_by_email(db: Session, email: str) -> Account|None:
    return db.query(Account).filter(Account.email == email).first()


def get_account_list(db: Session, skip: int = 0, limit: int = 10) -> List[Account]|None:
    return db.query(Account).offset(skip).limit(limit).all()


def create_account(db: Session, account: AccountCreate, user: Optional[UserCreate] = None) -> Account:
    hashed_password = get_password_hash(account.password)

    new_user = UserCreate()
    if user:
        new_user = user

    db_user =  _create_user(db, new_user)
    db_account = Account(email=account.email, hashed_password=hashed_password, user_id = db_user.id)

    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return db_account


def create_profile(db: Session, profile: ProfileCreate) -> Profile|None:
    db_profile = Profile(**profile.model_dump())

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    return db_profile


def get_profile(db: Session, user_id: int) -> Profile|None:
    return db.query(Profile).filter(Profile.user_id == user_id).first()


def get_permissions(db: Session, user_id: int) -> Set[Permission]|None:
    user = db.query(User).filter(User.id == user_id).first()
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


def authenticate(db: Session, email: str, password: str) -> User|None:
    db_user = get_account_by_email(db, email)
    if db_user and verify_password(password, cast(str, db_user.hashed_password)):
        return db_user
