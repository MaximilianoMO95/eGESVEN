from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.db import SessionLocal, engine
from app import schemas, crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users/", response_model=list[schemas.user.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.user.get_users(db, skip=skip, limit=limit)
    return users
