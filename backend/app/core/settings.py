import secrets
from typing import Literal, cast
from dotenv import load_dotenv
import os


load_dotenv()


AllowedEnvironments = Literal["local", "staging", "production"]


API_VERSION = "/api/v1"
DEFAULT_ROLE_NAME = "client"
ACCESS_TOKEN_EXPIRE_MINUTES = (60 * 24 * 8)
ENVIRONMENT: AllowedEnvironments = cast(AllowedEnvironments, os.getenv("ENVIRONMENT", "local"))
SQLALCHEMY_DATABASE_URL: str = "sqlite:///local.db"
SECRET_KEY = secrets.token_urlsafe(32)


if ENVIRONMENT != "local":
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", SQLALCHEMY_DATABASE_URL)
    if not SQLALCHEMY_DATABASE_URL:
        raise EnvironmentError(f"Required environment variable -> 'DATABASE_URL' is not set.")


    SECRET_KEY = os.getenv("SECRET_KEY", SECRET_KEY)
    if not SECRET_KEY:
        raise EnvironmentError(f"Required environment variable -> 'SECRET_KEY' is not set.")
