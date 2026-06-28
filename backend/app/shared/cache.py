import json
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator
import redis.asyncio as aioredis

class RedisCacheManager:
    def __init__(self) -> None:
        self._redis: aioredis.Redis | None = None

    def init(self, url: str) -> None:
        pool = aioredis.ConnectionPool.from_url(
            url,
            max_connections=50,
            decode_responses=False # Keep bytes for versatility
        )
        self._redis = aioredis.Redis(connection_pool=pool)

    async def close(self) -> None:
        if self._redis:
            await self._redis.aclose()
            self._redis = None

    async def get(self, key: str) -> bytes | None:
        if not self._redis:
            raise Exception("Redis is not initialized.")
        return await self._redis.get(key)

    async def get_json(self, key: str) -> Any | None:
        val = await self.get(key)
        if val:
            return json.loads(val.decode("utf-8"))
        return None

    async def set(self, key: str, value: bytes | str, ttl: int | None = None) -> None:
        if not self._redis:
            raise Exception("Redis is not initialized.")
        await self._redis.set(key, value, ex=ttl)

    async def set_json(self, key: str, value: Any, ttl: int | None = None) -> None:
        serialized = json.dumps(value)
        await self.set(key, serialized, ttl)

    async def delete(self, key: str) -> None:
        if not self._redis:
            raise Exception("Redis is not initialized.")
        await self._redis.delete(key)

    async def publish(self, channel: str, message: str) -> None:
        if not self._redis:
            raise Exception("Redis is not initialized.")
        await self._redis.publish(channel, message)

    @asynccontextmanager
    async def pubsub(self) -> AsyncIterator[aioredis.client.PubSub]:
        if not self._redis:
            raise Exception("Redis is not initialized.")
        ps = self._redis.pubsub()
        try:
            yield ps
        finally:
            await ps.aclose()

cache_manager = RedisCacheManager()

async def get_cache() -> RedisCacheManager:
    """FastAPI dependency for accessing the cache helper."""
    return cache_manager