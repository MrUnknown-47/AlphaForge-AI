import pytest
from app.modules.auth.schemas import UserCreate, UserLogin
from app.modules.auth.service import AuthService
from app.modules.auth.exceptions import PasswordValidationException, InvalidCredentialsException
from app.modules.auth.repository import AuthRepository

@pytest.mark.asyncio
async def test_password_length_validation(db_session):
    repo = AuthRepository(db_session)
    service = AuthService(repo)

    # 1. Short password (< 8 chars)
    short_data = UserCreate(
        email="short@example.com",
        username="shortuser",
        password="short"
    )
    with pytest.raises(PasswordValidationException):
        await service.register(short_data)

    # 2. Normal password (e.g. 12 chars)
    normal_data = UserCreate(
        email="normal@example.com",
        username="normaluser",
        password="normalpassword123"
    )
    user = await service.register(normal_data)
    assert user.email == "normal@example.com"

    # 3. 100 character password
    long_pass = "a" * 100
    long_data = UserCreate(
        email="long@example.com",
        username="longuser",
        password=long_pass
    )
    user_long = await service.register(long_data)
    assert user_long.email == "long@example.com"

    # 4. Too long password (> 128 chars)
    too_long_pass = "a" * 130
    too_long_data = UserCreate(
        email="toolong@example.com",
        username="toolonguser",
        password=too_long_pass
    )
    with pytest.raises(PasswordValidationException):
        await service.register(too_long_data)

    # 5. Unicode password
    unicode_pass = "secure🔑pásswörd!"
    unicode_data = UserCreate(
        email="unicode@example.com",
        username="unicodeuser",
        password=unicode_pass
    )
    user_unicode = await service.register(unicode_data)
    assert user_unicode.email == "unicode@example.com"

    # 6. Login verification
    login_data = UserLogin(
        email="unicode@example.com",
        password=unicode_pass
    )
    tokens = await service.authenticate(login_data)
    assert tokens.access_token is not None
    assert tokens.refresh_token is not None

    # 7. Refresh token flow
    rotated_tokens = await service.refresh(tokens.refresh_token)
    assert rotated_tokens.access_token is not None
    assert rotated_tokens.refresh_token is not None
