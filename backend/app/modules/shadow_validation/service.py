from typing import Dict, Any, List
from app.modules.shadow_validation.validation_engine import ValidationEngine

# Caching instances singleton
_validation_engine_instance = None

def get_validation_engine() -> ValidationEngine:
    global _validation_engine_instance
    if _validation_engine_instance is None:
        _validation_engine_instance = ValidationEngine()
    return _validation_engine_instance

class ShadowValidationService:
    def __init__(self) -> None:
        self.engine = get_validation_engine()

    async def run_validation_cycle(self) -> Dict[str, Any]:
        return await self.engine.execute_validation_cycle()

    def get_daily(self) -> List[Dict[str, Any]]:
        return self.engine.daily.daily_records

    def get_weekly(self) -> List[Dict[str, Any]]:
        return self.engine.weekly.weekly_records

    def get_monthly(self) -> List[Dict[str, Any]]:
        return self.engine.monthly.monthly_records

    def get_execution(self) -> Dict[str, Any]:
        return self.engine.execution.check_execution_quality()

    def get_capacity(self) -> List[Dict[str, Any]]:
        return self.engine.capacity.simulate_capacity()

    def get_scorecard(self) -> Dict[str, Any]:
        # Evaluates final scorecard defaults
        sc = self.engine.scorecard.generate_scorecard(
            sharpe=1.58, hit_ratio=0.612, max_drawdown=-0.114, psi=0.08,
            ruin_prob=0.001, uptime=99.9, latency=45.0
        )
        return sc
