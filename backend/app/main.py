from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints.main import api_router
from app.core import settings
from app.core.db import engine
from app import models


models.Base.metadata.create_all(bind=engine)

origins = ["*"]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_VERSION)
