import time
from typing import Dict, List

class APIRateLimiter:
    def __init__(self) -> None:
        self.request_history: Dict[str, List[float]] = {}
        self.limits = {
            "/login": (5, 60.0),      # 5 requests per 60s
            "/orders": (20, 60.0),     # 20 requests per 60s
            "/dashboard": (100, 60.0)  # 100 requests per 60s
        }

    def check_limit(self, client_ip: str, endpoint: str) -> bool:
        """Enforces sliding window rate-limits; returns True if request is allowed."""
        key = f"{client_ip}:{endpoint}"
        limit_count, limit_window = self.limits.get(endpoint, (100, 60.0))
        
        now = time.time()
        history = self.request_history.get(key, [])
        
        # Filter older than window
        history = [t for t in history if now - t < limit_window]
        
        if len(history) >= limit_count:
            return False
            
        history.append(now)
        self.request_history[key] = history
        return True
