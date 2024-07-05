from typing import cast
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import AccountCreate, UserPublic, UserRegister
from app.crud import user_crud
from .deps import get_db


router = APIRouter()


@router.post("/signup", response_model=UserPublic)
def register_user(user_in: UserRegister, db: Session = Depends(get_db)):
    user = user_crud.get_account_by_email(db, user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    account_create = AccountCreate(email=user_in.email, password=user_in.password)
    account = user_crud.create_account(db, account=account_create)

    user = user_crud.get_user(db, cast(int, account.user_id))
    return user
