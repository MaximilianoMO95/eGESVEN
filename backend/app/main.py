from fastapi import FastAPI

from app.core.db import engine
from app.endpoints import account, basket, login, product, category
from app import models


app = FastAPI()

app.include_router(account.router, prefix="/api/v1", tags=["account"])
app.include_router(product.router, prefix="/api/v1", tags=["product"])
app.include_router(category.router, prefix="/api/v1", tags=["category"])
app.include_router(basket.router, prefix="/api/v1", tags=["basket"])
app.include_router(login.router, prefix="/api/v1", tags=["login"])


# Create database tables
models.Base.metadata.create_all(bind=engine)
