from fastapi import FastAPI

from app.core.db import engine
from app.endpoints import user, product
from app import models


app = FastAPI()

app.include_router(user.router, prefix="/api/v1", tags=["user"])
app.include_router(product.router, prefix="/api/v1", tags=["product"])


# Create database tables
models.Base.metadata.create_all(bind=engine)
