from fastapi import FastAPI

from app.core.db import engine
from app.endpoints import user
from app import models


app = FastAPI()

app.include_router(user.router, prefix="/api/v1", tags=["user"])


# Create database tables
models.Base.metadata.create_all(bind=engine)
