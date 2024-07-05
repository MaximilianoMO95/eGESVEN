from functools import wraps
from typing import Any, cast
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.endpoints.deps import get_db, CurrentUser
from app.models.user import Permission, Role


def permission_required(permission_name: str, description: str = ""):
    """
    A decorator that registers a permission in the database and checks if the current user has the required permission.

    Args:
        permission_name (str): The name of the permission required for the route.
        description (str): A brief description of the permission (optional).

    Returns:
        The decorated route function.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper( *args: Any, db: Session, current_user: CurrentUser, **kwargs: Any) -> Any:
            # Check if the user has the required permission
            user_permissions = get_current_user_permissions(db, current_user)
            if permission_name not in user_permissions:
                raise HTTPException(status_code=403, detail="You do not have the required permissions")

            return await func(*args, **kwargs)


        _ = register_permission_in_db(permission_name, description)

        # Add the required permission to the route
        wrapper.__permission__ = permission_name
        return wrapper

    return decorator


def register_permission_in_db(permission_name: str, description: str) -> None:
    db: Session = next(get_db())

    permission = db.query(Permission).filter(Permission.name == permission_name).first()
    if not permission:
        permission = Permission(name=permission_name, description=description)
        db.add(permission)
        db.commit()
        db.refresh(permission)


def get_current_user_permissions(db: Session, current_user: CurrentUser) -> list[str]:
    user_role = db.query(Role).filter(Role.id == current_user.role_id).first()
    if not user_role:
        raise HTTPException(status_code=403, detail="No role assigned")

    permissions = db.query(Permission).join(Role.permissions).filter(Role.id == user_role.id).all()
    return [cast(str, perm.name) for perm in permissions]
