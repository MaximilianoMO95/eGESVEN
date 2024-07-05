from app.core.security import get_password_hash, verify_password, pwd_context


def test_get_password_hash():
    password = "password123"
    hashed_password = get_password_hash(password)

    assert hashed_password != password
    assert len(hashed_password) > 0
    assert pwd_context.verify(password, hashed_password)


def test_verify_password():
    plain_password = "password123"
    hashed_password = get_password_hash(plain_password)

    assert verify_password(plain_password, hashed_password)
    assert not verify_password("wrongpassword", hashed_password)
