from sqlalchemy import Boolean, Column, Integer, String

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(80))
    is_active = Column(Boolean, default=True)
