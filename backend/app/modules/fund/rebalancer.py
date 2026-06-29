import logging
from typing import Dict, Any, List

logger = logging.getLogger("FundRebalancer")

class FundRebalancer:
    def __init__(self) -> None:
        pass

    def check_drift_and_rebalance(
        self, current_weights: Dict[str, float], target_weights: Dict[str, float], threshold: float = 0.05
    ) -> bool:
        """Triggers rebalance if any asset drift exceeds the trigger threshold."""
        for asset, target in target_weights.items():
            curr = current_weights.get(asset, 0.0)
            if abs(curr - target) > threshold:
                logger.info(f"Fund rebalance triggered: {asset} drift of {abs(curr-target):.2%} exceeds limit.")
                return True
        return False
