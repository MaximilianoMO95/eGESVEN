from typing import cast
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.tests.utils.user import create_random_user, empty_user_records


def test_create_user(client: TestClient) -> None:
    user_data = {
        "email": "testuser@test.com",
        "password": "testpassword",
    }

    response = client.post("/users/", json=user_data)
    assert response.status_code == 200

    data = response.json()
    assert data["email"] == user_data["email"]
    assert not "password" in data


def test_get_users(client: TestClient, db: Session) -> None:
    empty_user_records(db)
    user_head = create_random_user(db)
    _ = create_random_user(db)
    _ = create_random_user(db)
    user_tail = create_random_user(db)

    response = client.get("/users/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 1

    assert any(u["email"] == cast(str, user_head.email) for u in data)
    assert any(u["email"] == cast(str, user_tail.email) for u in data)
