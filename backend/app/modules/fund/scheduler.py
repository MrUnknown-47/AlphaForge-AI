from datetime import datetime, timedelta
from typing import Dict, Any

class RebalanceScheduler:
    def __init__(self) -> None:
        pass

    def get_next_rebalance_time(self, frequency: str = "daily") -> datetime:
        now = datetime.utcnow()
        if frequency == "weekly":
            return now + timedelta(days=7)
        elif frequency == "monthly":
            return now + timedelta(days=30)
        return now + timedelta(days=1)
