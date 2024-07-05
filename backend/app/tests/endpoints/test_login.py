from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.crud import user_crud
from app.schemas.user import AccountCreate



def test_login_access_token(client: TestClient, db: Session):
    test_email = "test@example.com"
    test_password = "password123"

    user_crud.create_account(db, AccountCreate(email=test_email, password=test_password))
    response = client.post(
        "/login/access-token",
        data={ "username": test_email, "password": test_password },
    )
    assert response.status_code == 200

    json_response = response.json()
    assert "access_token" in json_response
    assert "expires_at" in json_response
    assert json_response["access_token"] is not None
