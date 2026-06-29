import logging
from typing import Dict, Any, List

logger = logging.getLogger("PortfolioRebalancer")

class PortfolioRebalancer:
    def __init__(self) -> None:
        pass

    def evaluate_rebalance_trigger(
        self, current_weights: Dict[str, float], target_weights: Dict[str, float],
        drawdown: float, volatility: float, threshold: float = 0.05
    ) -> bool:
        """Determines if current weights drift or drawdowns trigger rebalance."""
        # 1. Check drawdown trigger (rebalance if drawdown > 5%)
        if abs(drawdown) > 0.05:
            logger.info("Event-driven rebalance triggered: Drawdown limit breach.")
            return True

        # 2. Check volatility trigger (rebalance if volatility spikes > 25%)
        if volatility > 0.25:
            logger.info("Event-driven rebalance triggered: High Volatility breach.")
            return True

        # 3. Check weight drift trigger
        for symbol, target in target_weights.items():
            curr = current_weights.get(symbol, 0.0)
            if abs(curr - target) > threshold:
                logger.info(f"Drift rebalance triggered: {symbol} drift {abs(curr-target):.2%} exceeds threshold.")
                return True

        return False
