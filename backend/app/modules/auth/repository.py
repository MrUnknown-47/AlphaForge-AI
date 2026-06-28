import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.modules.auth.models import UserModel, SessionModel

class AuthRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_email(self, email: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def get_user_by_username(self, username: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.username == username)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def create_user(self, user: UserModel) -> UserModel:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def create_session(self, session: SessionModel) -> SessionModel:
        self.db.add(session)
        await self.db.commit()
        await self.db.refresh(session)
        return session

    async def get_session(self, refresh_token: str) -> SessionModel | None:
        stmt = select(SessionModel).where(SessionModel.refresh_token == refresh_token)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def delete_session(self, refresh_token: str) -> None:
        stmt = select(SessionModel).where(SessionModel.refresh_token == refresh_token)
        result = await self.db.execute(stmt)
        session = result.scalars().first()
        if session:
            await self.db.delete(session)
            await self.db.commit()

    async def create_revoked_token(self, token: str) -> None:
        from app.modules.auth.models import RevokedTokenModel
        model = RevokedTokenModel(token=token)
        self.db.add(model)
        await self.db.commit()

    async def is_token_revoked(self, token: str) -> bool:
        from app.modules.auth.models import RevokedTokenModel
        stmt = select(RevokedTokenModel).where(RevokedTokenModel.token == token)
        result = await self.db.execute(stmt)
        return result.scalars().first() is not None