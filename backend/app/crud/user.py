from sqlalchemy.orm import Session
from app.models.user import User, Role

from typing import List

from app.schemas.user import UserCreate


class UserCrud(object):
    @staticmethod
    def get_user(db: Session, user_id: int) -> User|None:
        return db.query(User).filter(User.id == user_id).first()


    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User|None:
        return db.query(User).filter(User.email == email).first()


    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]|None:
        return db.query(User).offset(skip).limit(limit).all()


    @staticmethod
    def create_user(db: Session, user: UserCreate):
        # TODO: Implement password hashing (SHA256)
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(email=user.email, hashed_password=fake_hashed_password)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


class RoleCrud(object):
    @staticmethod
    def create_role(db: Session, role_name: str) -> Role:
        db_role = Role(name=role_name)

        db.add(db_role)
        db.commit()
        db.refresh(db_role)

        return db_role


    @staticmethod
    def get_role(db: Session, role_id: int) -> Role|None:
        return db.query(Role).filter(Role.id == role_id).first()


    @staticmethod
    def get_roles(db: Session, skip: int = 0, limit: int = 10) -> List[Role]|None:
        return db.query(Role).offset(skip).limit(limit).all()


    @staticmethod
    def update_role(db: Session, role_id: int, new_name: str) -> Role|None:
        db_role = db.query(Role).filter(Role.id == role_id).first()
        if db_role:
            db_role.name = new_name
            db.commit()
            db.refresh(db_role)
            return db_role


    @staticmethod
    def delete_role(db: Session, role_id: int) -> Role|None:
        db_role = db.query(Role).filter(Role.id == role_id).first()
        if db_role:
            db.delete(db_role)
            db.commit()

            return db_role
