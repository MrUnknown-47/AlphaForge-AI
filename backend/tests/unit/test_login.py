import pytest
from app.modules.auth.schemas import UserLogin
from app.modules.auth.service import AuthService
from app.modules.auth.exceptions import InvalidCredentialsException

@pytest.mark.asyncio
async def test_authenticate_user_invalid(db_session):
    from app.modules.auth.repository import AuthRepository
    repo = AuthRepository(db_session)
    service = AuthService(repo)
    
    login_data = UserLogin(email="nonexistent@example.com", password="password123")
    with pytest.raises(InvalidCredentialsException):
        await service.authenticate(login_data)
