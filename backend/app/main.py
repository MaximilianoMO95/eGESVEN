from fastapi import FastAPI

from app.endpoints.main import api_router
from app.core import settings
from app.core.db import engine
from app import models


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(api_router, prefix=settings.API_VERSION)
