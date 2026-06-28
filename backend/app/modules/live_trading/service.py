from typing import List, Dict, Any
from app.modules.live_trading.scheduler import LiveScheduler

# Cached instance singleton
_live_scheduler_instance = None

def get_live_scheduler() -> LiveScheduler:
    global _live_scheduler_instance
    if _live_scheduler_instance is None:
        _live_scheduler_instance = LiveScheduler()
    return _live_scheduler_instance

class LiveTradingService:
    def __init__(self) -> None:
        self.scheduler = get_live_scheduler()

    async def run_cycle(self) -> None:
        await self.scheduler.execute_hourly_cycle()

    def get_predictions(self) -> List[Dict[str, Any]]:
        return [p.model_dump() for p in self.scheduler.predictions_store]

    def get_signals(self) -> List[Dict[str, Any]]:
        return [s.model_dump() for s in self.scheduler.signals_store]

    def get_metrics(self) -> List[Dict[str, Any]]:
        return [m.model_dump() for m in self.scheduler.metrics_store]

    def get_alerts(self) -> List[Dict[str, Any]]:
        return [a.model_dump() for a in self.scheduler.alerts_store]
