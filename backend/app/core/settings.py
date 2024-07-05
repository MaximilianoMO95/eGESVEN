import secrets
from dotenv import load_dotenv
import os


load_dotenv()


API_VERSION = "api/v1"
DEFAULT_ROLE_NAME = "client"
ACCESS_TOKEN_EXPIRE_MINUTES = (60 * 24 * 8)


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise EnvironmentError(f"Required environment variable -> 'DATABASE_URL' is not set.")


SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = secrets.token_urlsafe(32)
