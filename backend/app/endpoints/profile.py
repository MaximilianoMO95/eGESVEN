from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import ProfilePublic, ProfileCreate
from app.crud import user_crud
from .deps import get_db


router = APIRouter()


@router.post("/profiles", response_model=ProfilePublic)
def create_user_profile(user_profile: ProfileCreate, db: Session = Depends(get_db)):
    db_user_account = user_crud.get_account(db, user_id=user_profile.user_id)
    if db_user_account is None:
        raise HTTPException(status_code=404, detail="User account not found")

    return user_crud.create_profile(db=db, profile=user_profile)


@router.get("/profiles/{user_id}", response_model=ProfilePublic)
def read_user_profile(user_id: int, db: Session = Depends(get_db)):
    db_profile = user_crud.get_profile(db, user_id=user_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="User profile not found")

    return db_profile
