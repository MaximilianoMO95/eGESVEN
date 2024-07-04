from fastapi import FastAPI

from app.core.db import engine
from app.endpoints import account, product, category
from app import models


app = FastAPI()

app.include_router(account.router, prefix="/api/v1", tags=["account"])
app.include_router(product.router, prefix="/api/v1", tags=["product"])
app.include_router(category.router, prefix="/api/v1", tags=["category"])


# Create database tables
models.Base.metadata.create_all(bind=engine)
