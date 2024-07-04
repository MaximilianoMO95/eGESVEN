from sqlalchemy.orm import Session

from app.schemas.user import PermissionCreate
from app.models.user import Permission


def create(db: Session, permission: PermissionCreate) -> Permission | None:
    db_permission = Permission(name=permission.name, description=permission.description)
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission
