from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import AccountCreate, AccountPublic
from app.crud import user_crud
from app.endpoints.deps import get_db


router = APIRouter()


@router.post("/accounts/", response_model=AccountPublic)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_account_by_email(db, email=account.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return user_crud.create_account(db=db, account=account)


@router.get("/accounts/{user_id}", response_model=AccountPublic)
def read_account(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_account(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.get("/accounts/", response_model=list[AccountPublic])
def read_accounts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_crud.get_account_list(db=db, skip=skip, limit=limit)
