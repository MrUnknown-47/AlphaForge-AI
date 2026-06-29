import logging
import json
from typing import Optional, Any
from app.config import settings

logger = logging.getLogger("PortfolioCache")

class PortfolioCache:
    def __init__(self) -> None:
        self.redis_url = settings.REDIS_URL
        self.client = None
        self._local_cache = {}

        try:
            import redis
            self.client = redis.from_url(self.redis_url, socket_timeout=2.0)
            self.client.ping()
            logger.info("PortfolioCache connected to Redis successfully.")
        except Exception as e:
            logger.warning(f"Redis is unavailable: {e}. Falling back to local portfolio caching.")
            self.client = None

    def get(self, key: str) -> Optional[Any]:
        if self.client:
            try:
                data = self.client.get(key)
                if data:
                    return json.loads(data)
            except Exception as e:
                logger.error(f"Redis get failed: {e}")
        return self._local_cache.get(key)

    def set(self, key: str, value: Any, ttl: int) -> None:
        if self.client:
            try:
                self.client.setex(key, ttl, json.dumps(value))
                return
            except Exception as e:
                logger.error(f"Redis set failed: {e}")
        self._local_cache[key] = value
