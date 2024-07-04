from typing import cast
from sqlalchemy.orm import Session

from app.crud import user_crud, role_crud, permission_crud
from app.schemas.user import PermissionCreate, RoleCreate, AccountCreate

import app.tests.utils as utils


def test_create_user_account(db: Session) -> None:
    new_account = AccountCreate(email="test@example.com", password="password123")

    account = user_crud.create_account(db, new_account)
    assert account.id is not None
    assert cast(str, account.email) == new_account.email


def test_get_account(db: Session) -> None:
    target_account = utils.user.create_random_user_account(db)

    account = user_crud.get_account_by_email(db, "fake@fake.cl")
    assert account is None

    account = user_crud.get_account_by_email(db, cast(str, target_account.email))
    assert account is not None


def test_get_user_accounts(db: Session) -> None:
    account_head = utils.user.create_random_user_account(db)
    _ = utils.user.create_random_user_account(db)
    _ = utils.user.create_random_user_account(db)
    _ = utils.user.create_random_user_account(db)
    account_tail = utils.user.create_random_user_account(db)

    accounts = user_crud.get_account_list(db)
    assert accounts is not None
    assert len(accounts) > 1

    assert any(cast(str, u.email) == cast(str, account_head.email) for u in accounts)
    assert any(cast(str, u.email) == cast(str, account_tail.email) for u in accounts)


def test_create_role(db: Session) -> None:
    role_create = RoleCreate(name="admin")

    role = role_crud.create(db, role_create)
    assert role is not None
    assert cast(str, role.name) == role_create.name


def test_get_role(db: Session) -> None:
    target_role = utils.user.create_random_role(db)

    role = role_crud.get_by_name(db, cast(str, target_role.name))
    assert role is not None
    assert cast(str, role.name) == cast(str, target_role.name)

    role = role_crud.get(db, cast(int, target_role.id))
    assert role is not None
    assert cast(str, role.name) == cast(str, target_role.name)


def test_create_permission(db: Session) -> None:
    permission_create = PermissionCreate(name="view", description="Can view resources")

    permission = permission_crud.create(db, permission_create)
    assert permission is not None
    assert cast(str, permission.name) == permission_create.name
    assert cast(str, permission.description) == permission_create.description


def test_user_permissions(db: Session) -> None:
    account = utils.user.create_random_user_account(db)
    user = user_crud.get_user(db, cast(int, account.user_id))

    permission_create = PermissionCreate(name="edit", description="Can edit resources")
    permission = permission_crud.create(db, permission_create)

    assert user is not None
    assert permission is not None

    _ = role_crud.add_permission(db, cast(int, user.role_id), permission_create)

    permissions = user_crud.get_permissions(db, cast(int, user.id))
    assert permissions is not None
    assert "edit" in permissions


def test_have_permission(db: Session) -> None:
    account = utils.user.create_random_user_account(db)
    user = user_crud.get_user(db, cast(int, account.user_id))
    assert user is not None

    _ = permission_crud.create(
        db,
        PermissionCreate(name="delete", description="Can delete resources")
    )
    _ = role_crud.add_permission(
        db,
        cast(int, user.role_id),
        PermissionCreate(name="edit", description="Can edit resources")
    )

    edit_permission = user_crud.have_permission(db, cast(int, user.id), "edit")
    delete_permission = user_crud.have_permission(db, cast(int, user.id), "delete")
    assert edit_permission is True
    assert delete_permission is False


def test_update_role(db: Session) -> None:
    target_role = utils.user.create_random_role(db)
    new_name = "superadmin"

    updated_role = role_crud.update(db, cast(int, target_role.id), new_name)
    assert updated_role is not None
    assert cast(str, updated_role.id) == cast(int, target_role.id)
    assert cast(str, updated_role.name) == cast(str, target_role.name)


def test_delete_role(db: Session) -> None:
    target_role = utils.user.create_random_role(db)

    deleted_role = role_crud.delete(db, cast(int, target_role.id))
    assert deleted_role is not None
    assert cast(str, deleted_role.name) == cast(str, target_role.name)

    still_around = role_crud.get_by_name(db, cast(str, target_role.name))
    assert still_around is None
