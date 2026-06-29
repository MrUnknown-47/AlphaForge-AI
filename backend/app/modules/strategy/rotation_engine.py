import logging
from typing import Dict, Any, List
from app.modules.strategy.ranking_engine import StrategyRankingEngine
from app.modules.strategy.weight_engine import StrategyWeightEngine

logger = logging.getLogger("StrategyRotationEngine")

class StrategyRotationEngine:
    def __init__(self) -> None:
        self.ranker = StrategyRankingEngine()
        self.weighter = StrategyWeightEngine()

    def run_strategy_rotation(self) -> Dict[str, float]:
        """Calculates current strategy rotation weights."""
        ranked = self.ranker.rank_strategies()
        weights = self.weighter.compute_strategy_weights(ranked)
        logger.info(f"Generated new strategy rotation allocation weights: {weights}")
        return weights
