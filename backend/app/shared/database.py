from contextlib import asynccontextmanager
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import event

class Base(DeclarativeBase):
    """Declarative Base class that supports custom database schemas."""
    pass

@event.listens_for(Base.metadata, "before_create")
def sqlite_schema_mapping(target, connection, **kw):
    if connection.dialect.name == "sqlite":
        # Rename table names to insert schema prefix in SQLite
        for table in target.tables.values():
            if table.schema:
                table.name = f"{table.schema}_{table.name}"
                table.schema = None



class DatabaseSessionManager:
    def __init__(self) -> None:
        self._engine = None
        self._sessionmaker = None

    def init(self, host: str) -> None:
        # Check for SQLite fallback to support offline testing
        if "sqlite" in host:
            self._engine = create_async_engine(host)
        else:
            self._engine = create_async_engine(
                host,
                pool_pre_ping=True,
                pool_size=20,
                max_overflow=10
            )
        self._sessionmaker = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine,
            expire_on_commit=False
        )

    async def close(self) -> None:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized.")
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized.")
        session = self._sessionmaker()
        try:
            yield session
        finally:
            await session.close()

    @asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized.")
        async with self._engine.begin() as connection:
            yield connection

db_manager = DatabaseSessionManager()

async def get_db() -> AsyncIterator[AsyncSession]:
    """FastAPI Dependency injector for fetching DB sessions."""
    async with db_manager.session() as session:
        yield session