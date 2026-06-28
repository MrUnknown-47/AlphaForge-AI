import asyncio
import pytest
import pytest_asyncio
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.shared.database import Base
from app.shared.cache import cache_manager

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="session")
async def db_engine():
    # SQLite in-memory or ephemeral PostgreSQL testcontainer URL
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest_asyncio.fixture
async def db_session(db_engine) -> AsyncIterator[AsyncSession]:
    session_maker = async_sessionmaker(bind=db_engine, expire_on_commit=False)
    async with session_maker() as session:
        yield session

@pytest_asyncio.fixture(scope="session")
async def redis_client():
    # In production tests, this initializes a Redis Testcontainer
    cache_manager.init("redis://localhost:6379/0")
    yield cache_manager
    await cache_manager.close()