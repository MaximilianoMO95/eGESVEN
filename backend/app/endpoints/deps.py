from typing import Any, Generator
from sqlalchemy.orm import Session
from app.core.db import SessionLocal


def get_db() -> Generator[Session, Any, None]:
    with SessionLocal() as db:
        try: yield db
        finally: db.close()
