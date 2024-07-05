from datetime import timedelta
import jwt

from app.core import security, settings


def test_create_access_token():
    subject = "user_id"
    expires_delta = timedelta(minutes=15)
    token = security.create_access_token(subject, expires_delta)
    decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])

    assert decoded_token["sub"] == subject
    assert "exp" in decoded_token
