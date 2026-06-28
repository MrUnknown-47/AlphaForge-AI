import pytest
from app.modules.auth.service import AuthService

@pytest.mark.asyncio
async def test_logout_session_invalidation(db_session):
    from app.modules.auth.repository import AuthRepository
    repo = AuthRepository(db_session)
    service = AuthService(repo)
    
    # Invalidation shouldn't raise exceptions for non-existent token
    await service.invalidate("random_nonexistent_token")
