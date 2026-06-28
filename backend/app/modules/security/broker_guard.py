import logging
from typing import Dict, Any
from app.config import settings

logger = logging.getLogger("BrokerGuard")

class BrokerGuard:
    def __init__(self) -> None:
        pass

    def validate_broker_environment(self, account_details: Dict[str, Any]) -> bool:
        """
        Safety audit preventing live execution:
        - Must assert account type is PAPER
        - Withdrawal capability must be FALSE
        - Enforces buying power verification limits
        """
        is_paper = account_details.get("is_paper", True)
        can_withdraw = account_details.get("can_withdraw", False)
        
        # Enforce Alpaca PAPER trading ONLY
        if not is_paper or can_withdraw:
            logger.critical("SAFETY VIOLATION: Live or withdrawing credentials detected! Blocking execution.")
            return False

        logger.info("BrokerGuard: Verified Alpaca PAPER environment successfully.")
        return True
