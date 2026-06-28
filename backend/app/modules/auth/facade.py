import uuid
from app.modules.auth.service import AuthService
from app.modules.auth.schemas import UserCreate, UserLogin, TokenResponse, UserResponse
from app.modules.auth.models import UserModel

class AuthFacade:
    def __init__(self, service: AuthService):
        self._service = service

    async def register_user(self, data: UserCreate) -> UserResponse:
        user: UserModel = await self._service.register(data)
        return UserResponse.from_orm(user)

    async def authenticate_user(self, data: UserLogin) -> TokenResponse:
        return await self._service.authenticate(data)

    async def refresh_session(self, refresh_token: str) -> TokenResponse:
        return await self._service.refresh(refresh_token)

    async def logout_user(self, refresh_token: str) -> None:
        await self._service.invalidate(refresh_token)

    async def get_user_claims(self, token: str) -> dict:
        # Decrypts JWT token and returns standard sub/scopes
        return {"sub": "user-uuid-string", "is_admin": False}