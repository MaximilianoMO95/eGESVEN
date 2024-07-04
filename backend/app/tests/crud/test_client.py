from typing import cast
from sqlalchemy.orm import Session
import pytest

from app.crud import client_crud
from app.schemas.user import ClientCreate
from app.tests.utils.user import create_random_user_account


@pytest.fixture
def client_data(db: Session) -> ClientCreate:
    account = create_random_user_account(db)

    return ClientCreate(
        user_id=cast(int, account.id),
    )


def test_create_client(db: Session, client_data: ClientCreate):
    client = client_crud.create(db, client_data)
    assert client is not None

    assert cast(int, client.user_id) == cast(int, client_data.user_id)


def test_get_client(db: Session, client_data: ClientCreate):
    created_client = client_crud.create(db, client_data)
    assert created_client is not None

    fetched_client = client_crud.get(db, cast(int, created_client.user_id))
    assert fetched_client is not None
    assert cast(int, fetched_client.user_id) == cast(int, created_client.user_id)
