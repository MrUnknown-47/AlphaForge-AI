import uuid
from datetime import datetime, timedelta
from app.modules.auth.repository import AuthRepository
from app.modules.auth.schemas import UserCreate, UserLogin, TokenResponse
from app.modules.auth.models import UserModel, SessionModel
from app.modules.auth.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    SessionExpiredException,
)
from app.shared.cache import cache_manager

class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def hash_password(self, password: str) -> str:
        # Bcrypt implementation interface
        return f"hashed_{password}"  # Skeleton representation

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return hashed_password == f"hashed_{plain_password}"

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

        access_token = self.generate_jwt_access_token(user)
        refresh_token = str(uuid.uuid4())
        
        # Save session to DB
        expires_at = datetime.utcnow() + timedelta(days=7)
        session = SessionModel(
            user_id=user.id,
            refresh_token=refresh_token,
            expires_at=expires_at
        )
        await self.repo.create_session(session)

        # Cache session in Redis
        redis_client.setex(
            f"auth:session:{refresh_token}",
            int(timedelta(days=7).total_seconds()),
            str(user.id)
        )

        return TokenResponse(access_token=access_token, refresh_token=refresh_token)

    async def refresh(self, refresh_token: str) -> TokenResponse:
        # Check cache first
        user_id_bytes = redis_client.get(f"auth:session:{refresh_token}")
        
        if user_id_bytes is None:
            # Fallback to DB
            session = await self.repo.get_session(refresh_token)
            if not session or session.expires_at < datetime.utcnow():
                raise SessionExpiredException()
            user_id = session.user_id
        else:
            user_id = uuid.UUID(user_id_bytes.decode())

        # In a real environment, load user, issue new tokens, and update Redis
        access_token = f"new_jwt_for_{user_id}"
        new_refresh_token = str(uuid.uuid4())
        return TokenResponse(access_token=access_token, refresh_token=new_refresh_token)

    async def invalidate(self, refresh_token: str) -> None:
        redis_client.delete(f"auth:session:{refresh_token}")
        await self.repo.delete_session(refresh_token)

    def generate_jwt_access_token(self, user: UserModel) -> str:
        # Standard RS256 signature logic skeleton
        return f"jwt_access_token_for_{user.email}"