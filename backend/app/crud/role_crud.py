from sqlalchemy import Column
from sqlalchemy.orm import Session

from typing import List, cast

from app.schemas.user import PermissionCreate, RoleCreate
from app.models.user import Permission, Role


def create(db: Session, role: RoleCreate) -> Role:
    db_role = Role(name=role.name)

    db.add(db_role)
    db.commit()
    db.refresh(db_role)

    return db_role


def get(db: Session, role_id: int) -> Role|None:
    return db.query(Role).filter(Role.id == role_id).first()


def get_by_name(db: Session, name: str) -> Role|None:
    return db.query(Role).filter(Role.name == name).first()


def get_list(db: Session, skip: int = 0, limit: int = 10) -> List[Role]|None:
    return db.query(Role).offset(skip).limit(limit).all()


def update(db: Session, role_id: int, new_name: str) -> Role|None:
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        db_role.name = cast(Column[str], new_name)
        db.commit()
        db.refresh(db_role)
        return db_role


def delete(db: Session, role_id: int) -> Role|None:
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        db.delete(db_role)
        db.commit()

        return db_role


def add_permission(db: Session, role_id: int, permission: PermissionCreate) -> Role:
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


def remove_permission(db: Session, role_id: int, permission_name: str) -> Role:
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
