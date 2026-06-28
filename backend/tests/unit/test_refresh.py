import pytest
from app.modules.auth.service import AuthService
from app.modules.auth.exceptions import SessionExpiredException

@pytest.mark.asyncio
async def test_refresh_token_expired_or_invalid(db_session):
    from app.modules.auth.repository import AuthRepository
    repo = AuthRepository(db_session)
    service = AuthService(repo)
    
    with pytest.raises(SessionExpiredException):
        await service.refresh("invalid_or_expired_token")
