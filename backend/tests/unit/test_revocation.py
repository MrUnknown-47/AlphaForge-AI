import pytest
from app.modules.auth.service import AuthService

@pytest.mark.asyncio
async def test_token_revocation_lifecycle(db_session):
    from app.modules.auth.repository import AuthRepository
    repo = AuthRepository(db_session)
    service = AuthService(repo)
    
    test_token = "some_random_refresh_token_to_revoke"
    assert not await service.is_revoked(test_token)
    
    await service.revoke(test_token)
    assert await service.is_revoked(test_token)
