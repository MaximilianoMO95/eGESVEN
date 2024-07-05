from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import ClientPublic
from app.crud import client_crud
from backend.app.decorators.permission import permission_required
from .deps import get_db


router = APIRouter()


@router.get("/clients/{user_id}", response_model=ClientPublic)
@permission_required("read_client")
def read_client(user_id: int, db: Session = Depends(get_db)):
    db_client = client_crud.get(db=db, user_id=user_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")

    return db_client
