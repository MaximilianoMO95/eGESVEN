from typing import cast
from sqlalchemy.orm import Session

from app.crud.user import UserCrud as crud_user
from app.crud.user import RoleCrud as crud_role
from app.crud.user import PermissionCrud as crud_permission
from app.crud.user import RolePermissionCrud as crud_role_permission
from app.schemas.user import PermissionCreate, RoleCreate, UserCreate

import app.tests.utils as utils


def test_create_user(db: Session) -> None:
    user_create = UserCreate(email="test@example.com", password="password123")

    user = crud_user.create_user(db, user_create)
    assert user.id is not None
    assert cast(str, user.email) == user_create.email


def test_get_user(db: Session) -> None:
    target_user = utils.user.create_random_user(db)

    user = crud_user.get_user_by_email(db, "fake@fake.cl")
    assert user is None

    user = crud_user.get_user_by_email(db, cast(str, target_user.email))
    assert user is not None


def test_get_users(db: Session) -> None:
    user_head = utils.user.create_random_user(db)
    _ = utils.user.create_random_user(db)
    _ = utils.user.create_random_user(db)
    _ = utils.user.create_random_user(db)
    user_tail = utils.user.create_random_user(db)

    users = crud_user.get_users(db)
    assert users is not None
    assert len(users) > 1

    assert any(cast(str, u.email) == cast(str, user_head.email) for u in users)
    assert any(cast(str, u.email) == cast(str, user_tail.email) for u in users)


def test_create_role(db: Session) -> None:
    role_create = RoleCreate(name="admin")

    role = crud_role.create_role(db, role_create)
    assert role is not None
    assert cast(str, role.name) == role_create.name


def test_get_role(db: Session) -> None:
    target_role = utils.user.create_random_role(db)

    role = crud_role.get_role_by_name(db, cast(str, target_role.name))
    assert role is not None
    assert cast(str, role.name) == cast(str, target_role.name)

    role = crud_role.get_role(db, cast(int, target_role.id))
    assert role is not None
    assert cast(str, role.name) == cast(str, target_role.name)


def test_create_permission(db: Session) -> None:
    permission_create = PermissionCreate(name="view", description="Can view resources")

    permission = crud_permission.create_permission(db, permission_create)
    assert permission is not None
    assert cast(str, permission.name) == permission_create.name
    assert cast(str, permission.description) == permission_create.description


def test_user_permissions(db: Session) -> None:
    user = utils.user.create_random_user(db)

    permission_create = PermissionCreate(name="edit", description="Can edit resources")
    permission = crud_permission.create_permission(db, permission_create)

    assert user is not None
    assert permission is not None

    _ = crud_role_permission.add_permission_to_role(db, cast(int, user.role_id), permission_create)

    permissions = crud_user.get_user_permissions(db, cast(int, user.id))
    assert permissions is not None
    assert "edit" in permissions


def test_have_permission(db: Session) -> None:
    user = utils.user.create_random_user(db)

    _ = crud_permission.create_permission(
        db,
        PermissionCreate(name="delete", description="Can delete resources")
    )
    _ = crud_role_permission.add_permission_to_role(
        db,
        cast(int, user.role_id),
        PermissionCreate(name="edit", description="Can edit resources")
    )

    edit_permission = crud_user.have_permission(db, cast(int, user.id), "edit")
    delete_permission = crud_user.have_permission(db, cast(int, user.id), "delete")
    assert edit_permission is True
    assert delete_permission is False


def test_update_role(db: Session) -> None:
    target_role = utils.user.create_random_role(db)
    new_name = "superadmin"

    updated_role = crud_role.update_role(db, cast(int, target_role.id), new_name)
    assert updated_role is not None
    assert cast(str, updated_role.id) == cast(int, target_role.id)
    assert cast(str, updated_role.name) == cast(str, target_role.name)


def test_delete_role(db: Session) -> None:
    target_role = utils.user.create_random_role(db)

    deleted_role = crud_role.delete_role(db, cast(int, target_role.id))
    assert deleted_role is not None
    assert cast(str, deleted_role.name) == cast(str, target_role.name)

    still_around = crud_role.get_role_by_name(db, cast(str, target_role.name))
    assert still_around is None
