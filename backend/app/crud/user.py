from sqlalchemy import Column
from sqlalchemy.orm import Session
from app.models.user import User, Role, Permission

from typing import List, Set, cast

from app.schemas.user import PermissionCreate, RoleCreate, UserCreate


class UserCrud:

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
    def create_user(db: Session, user: UserCreate) -> User:
        # TODO: Implement password hashing (SHA256)
        fake_hashed_password = user.password + "notreallyhashed"

        role = RoleCrud.get_role_by_name(db, "client");
        if not role:
            role = RoleCrud.create_role(db, RoleCreate(name="client"));

        db_user = User(email=user.email, hashed_password=fake_hashed_password, role_id=role.id)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


    @staticmethod
    def get_user_permissions(db: Session, user_id: int) -> Set[Permission]|None:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None


        permissions = set()
        for role in user.role:
            for perm in role.permissions:
                permissions.add(perm.name)
        return permissions


    @staticmethod
    def have_permission(db: Session, user_id: int, permission: str) -> bool:
        permissions = UserCrud.get_user_permissions(db, user_id)
        if not permissions or permission not in permissions:
            return False

        return True


class RoleCrud:

    @staticmethod
    def create_role(db: Session, role: RoleCreate) -> Role:
        db_role = Role(name=role.name)

        db.add(db_role)
        db.commit()
        db.refresh(db_role)

        return db_role


    @staticmethod
    def get_role(db: Session, role_id: int) -> Role|None:
        return db.query(Role).filter(Role.id == role_id).first()


    @staticmethod
    def get_role_by_name(db: Session, name: str) -> Role|None:
        return db.query(Role).filter(Role.name == name).first()


    @staticmethod
    def get_roles(db: Session, skip: int = 0, limit: int = 10) -> List[Role]|None:
        return db.query(Role).offset(skip).limit(limit).all()


    @staticmethod
    def update_role(db: Session, role_id: int, new_name: str) -> Role|None:
        db_role = db.query(Role).filter(Role.id == role_id).first()
        if db_role:
            db_role.name = cast(Column[str], new_name)
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


class PermissionCrud:

    @staticmethod
    def create_permission(db: Session, permission: PermissionCreate):
        db_permission = Permission(name=permission.name, description=permission.description)
        db.add(db_permission)
        db.commit()
        db.refresh(db_permission)
        return db_permission


class RolePermissionCrud:

    @staticmethod
    def add_permission_to_role(db: Session, role_id: int, permission: PermissionCreate) -> Role:
        role = db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise ValueError("Role not found")

        # Check if the permission already exists
        existing_permission = db.query(Permission).filter(Permission.name == permission.name).first()
        if not existing_permission:
            existing_permission = Permission(name=permission.name, description=permission.description)
            db.add(existing_permission)
            db.commit()
            db.refresh(existing_permission)

        # Add permission to role if not already present
        if existing_permission not in role.permissions:
            role.permissions.append(existing_permission)
            db.commit()
            db.refresh(role)

        return role


    @staticmethod
    def remove_permission_from_role(db: Session, role_id: int, permission_name: str) -> Role:
        role = db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise ValueError("Role not found")

        # Find the permission to remove
        permission = db.query(Permission).filter(Permission.name == permission_name).first()
        if not permission:
            raise ValueError("Permission not found")

        if permission in role.permissions:
            role.permissions.remove(permission)
            db.commit()
            db.refresh(role)

        return role
