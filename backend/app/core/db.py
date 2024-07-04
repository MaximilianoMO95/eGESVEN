from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise EnvironmentError(f"Required environment variable -> 'DATABASE_URL' is not set.")


# Note: For SQLITE you have to aditionally pass "connect_args={"check_same_thread": False}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db(db: Session) -> None:
    from app.schemas.user import PermissionCreate, RoleCreate
    from app.crud import permission_crud, role_crud

    # Create default permissions
    client_permission = PermissionCreate(
        name="read_products",
        description="Permission to read products"
    )
    view_permission = permission_crud.create(db, client_permission)

    # Create default roles
    client_role = role_crud.create(db, RoleCreate(name="client"))
    client_role.permissions.append(view_permission)
