from typing import cast
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.crud import client_crud
from app.models.user import Client
from app.schemas.user import ClientCreate

from .user import create_random_user_account


def create_random_client(db: Session) -> Client:
    account = create_random_user_account(db)

    client = ClientCreate(user_id=cast(int, account.user_id))
    return client_crud.create(db, client)


def empty_client_records(db: Session) -> None:
    db.execute(delete(Client))
    db.commit()
