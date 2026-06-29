from typing import Dict, Any, List
from app.modules.strategy.alpha_engine import AlphaEngine

class StrategyRankingEngine:
    def __init__(self) -> None:
        self.alpha_engine = AlphaEngine()

    def rank_strategies(self) -> List[Dict[str, Any]]:
        """Ranks strategies dynamically by expected alpha forecast return."""
        forecasts = self.alpha_engine.generate_alpha_forecasts()
        ranked = sorted(forecasts.items(), key=lambda item: item[1], reverse=True)
        return [{"strategy": k, "expected_alpha": v} for k, v in ranked]
