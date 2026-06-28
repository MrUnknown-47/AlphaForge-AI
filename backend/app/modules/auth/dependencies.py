from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.auth.repository import AuthRepository
from app.modules.auth.service import AuthService
from app.modules.auth.facade import AuthFacade
from app.modules.auth.exceptions import UnauthorizedException, ForbiddenException

async def get_auth_repo(db: AsyncSession = Depends(get_db)) -> AuthRepository:
    return AuthRepository(db)

async def get_auth_service(repo: AuthRepository = Depends(get_auth_repo)) -> AuthService:
    return AuthService(repo)

async def get_auth_facade(service: AuthService = Depends(get_auth_service)) -> AuthFacade:
    return AuthFacade(service)

# Middleware verification dependencies
async def get_current_user(
    token: str, # Usually extracted from header (HTTPBearer)
    facade: AuthFacade = Depends(get_auth_facade)
) -> dict:
    try:
        claims = await facade.get_user_claims(token)
        return claims
    except Exception:
        raise UnauthorizedException()

async def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if not current_user.get("is_admin", False):
        raise ForbiddenException()
    return current_user
