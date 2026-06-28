import uuid
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from app.modules.auth.repository import AuthRepository
from app.modules.auth.schemas import UserCreate, UserLogin, TokenResponse
from app.modules.auth.models import UserModel, SessionModel
from app.modules.auth.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    SessionExpiredException,
)
from app.shared.cache import cache_manager
from app.modules.security.jwt_manager import JWTManager
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
jwt_manager = JWTManager(secret=settings.SECRET_KEY)

class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    async def register(self, data: UserCreate) -> UserModel:
        existing = await self.repo.get_user_by_email(data.email)
        if existing:
            raise UserAlreadyExistsException()
        
        hashed = self.hash_password(data.password)
        new_user = UserModel(
            email=data.email,
            username=data.username,
            password_hash=hashed
        )
        return await self.repo.create_user(new_user)

    async def authenticate(self, data: UserLogin) -> TokenResponse:
        user = await self.repo.get_user_by_email(data.email)
        if not user or not self.verify_password(data.password, user.password_hash):
            raise InvalidCredentialsException()

        access_token = jwt_manager.create_access_token({"sub": str(user.id), "username": user.username, "role": "ADMIN" if user.is_admin else "TRADER"})
        refresh_token = jwt_manager.create_refresh_token({"sub": str(user.id), "username": user.username})
        
        # Save session to DB
        expires_at = datetime.utcnow() + timedelta(days=7)
        session = SessionModel(
            user_id=user.id,
            refresh_token=refresh_token,
            expires_at=expires_at
        )
        await self.repo.create_session(session)

        # Cache session in Redis
        try:
            await cache_manager.set(
                f"auth:session:{refresh_token}",
                str(user.id),
                ttl=int(timedelta(days=7).total_seconds())
            )
        except Exception:
            pass

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="Bearer",
            expires_in=900
        )

    async def is_revoked(self, token: str) -> bool:
        # Check Redis first
        try:
            val = await cache_manager.get(f"auth:revoked:{token}")
            if val is not None:
                return True
        except Exception:
            pass
        # Fallback to DB
        return await self.repo.is_token_revoked(token)

    async def revoke(self, token: str) -> None:
        # Save in Redis revoked list
        try:
            await cache_manager.set(f"auth:revoked:{token}", "1", ttl=604800)
        except Exception:
            pass
        # Save in DB
        await self.repo.create_revoked_token(token)

    async def refresh(self, refresh_token: str) -> TokenResponse:
        payload = jwt_manager.verify_refresh_token(refresh_token)
        if not payload:
            raise SessionExpiredException()

        is_revoked = await self.is_revoked(refresh_token)
        if is_revoked:
            raise SessionExpiredException()

        # Invalidate old refresh token
        await self.revoke(refresh_token)
        await self.repo.delete_session(refresh_token)
        try:
            await cache_manager.delete(f"auth:session:{refresh_token}")
        except Exception:
            pass

        user_id = payload.get("sub")
        username = payload.get("username")

        # Generate new tokens (Rotation)
        access_token = jwt_manager.create_access_token({"sub": user_id, "username": username, "role": "TRADER"})
        new_refresh_token = jwt_manager.create_refresh_token({"sub": user_id, "username": username})

        # Save new session
        expires_at = datetime.utcnow() + timedelta(days=7)
        session = SessionModel(
            user_id=uuid.UUID(user_id),
            refresh_token=new_refresh_token,
            expires_at=expires_at
        )
        await self.repo.create_session(session)

        # Cache session in Redis
        try:
            await cache_manager.set(
                f"auth:session:{new_refresh_token}",
                user_id,
                ttl=int(timedelta(days=7).total_seconds())
            )
        except Exception:
            pass

        return TokenResponse(
            access_token=access_token,
            refresh_token=new_refresh_token,
            token_type="Bearer",
            expires_in=900
        )

    async def invalidate(self, refresh_token: str) -> None:
        try:
            await cache_manager.delete(f"auth:session:{refresh_token}")
        except Exception:
            pass
        await self.repo.delete_session(refresh_token)
        await self.revoke(refresh_token)

    def generate_jwt_access_token(self, user: UserModel) -> str:
        return jwt_manager.create_access_token({"sub": str(user.id), "username": user.username, "role": "TRADER"})