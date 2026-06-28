from typing import Dict, Any
from app.modules.validation.live_validator import LiveValidator

# Singleton cache
_live_validator_instance = None

def get_live_validator() -> LiveValidator:
    global _live_validator_instance
    if _live_validator_instance is None:
        _live_validator_instance = LiveValidator()
    return _live_validator_instance

class ValidationService:
    def __init__(self) -> None:
        self.validator = get_live_validator()

    async def run_validation_cycle(self) -> Dict[str, Any]:
        # Mock active prices
        prices = {"AAPL": 182.50, "MSFT": 420.10, "NVDA": 122.50}
        return await self.validator.execute_validation_cycle(prices)

    def get_performance_stats(self) -> Dict[str, Any]:
        return self.validator.performance.compute_rolling_metrics(30)

    def get_risk_stats(self) -> Dict[str, Any]:
        # Generate dummy stats mapping
        return self.validator.risk.analyze_risk_limits(100000.0, [], 0.0, -0.114)

    def get_drift_stats(self) -> Dict[str, Any]:
        return self.validator.drift.compute_drift_metrics()

    def get_scorecard(self) -> Dict[str, Any]:
        # Defaults to default values of scorecard generator
        sc = self.validator.scorecard.generate_scorecard(
            paper_days=30, sharpe=1.58, sortino=2.05, max_drawdown=-0.114,
            hit_ratio=0.612, profit_factor=1.65, psi=0.08, latency_ms=12.5, daily_loss=0.0
        )
        return sc
