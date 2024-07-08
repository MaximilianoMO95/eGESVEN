import os
import pytest

from typing import Any, Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv

from fastapi.testclient import TestClient

from app.endpoints.deps import get_db
from app.core.db import engine, Base, init_db
from app.main import app


load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
if not TEST_DATABASE_URL:
    raise EnvironmentError(f"Required environment variable -> 'TEST_DATABASE_URL' is not set.")


# Note: For SQLITE you have to aditionally pass "connect_args={"check_same_thread": False}"
engine = create_engine(TEST_DATABASE_URL)
if "sqlite://" in TEST_DATABASE_URL:
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the testing session
def overwrite_get_db():
    with TestingSessionLocal() as db:
        try: yield db
        finally: db.close()

app.dependency_overrides[get_db] = overwrite_get_db


 # Create the database tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, Any, None]:
    with TestClient(app) as c:
        c.base_url = c.base_url.join("/api/v1")
        yield c


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, Any, None]:
    with TestingSessionLocal() as session:
        init_db(session)

        yield session
        session.close()
