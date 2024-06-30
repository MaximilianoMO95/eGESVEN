from typing import cast
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.tests.utils.user import create_random_role, create_random_user


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
    role = create_random_role(db)

    _ = create_random_user(db, cast(int, role.id))
    _ = create_random_user(db, cast(int, role.id))
    user = create_random_user(db, cast(int, role.id))

    response = client.get("/users/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 1
    assert any(u["email"] == user.email for u in data)
