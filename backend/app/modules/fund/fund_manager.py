import logging
from typing import Dict, Any, List

logger = logging.getLogger("FundManager")

class FundManager:
    def __init__(self) -> None:
        self.nav = 105.42 # $105.42 Net Asset Value per share
        self.aum = 250000000.0 # $250M Assets Under Management
        self.leverage = 1.35 # 1.35x leverage ratio
        self.management_fee_rate = 0.02 # 2% management fee
        self.performance_fee_rate = 0.20 # 20% performance fee
        self.hurdle_rate = 0.05 # 5% hurdle rate

    def get_fund_metrics(self) -> Dict[str, Any]:
        return {
            "nav": self.nav,
            "aum": self.aum,
            "leverage": self.leverage,
            "fees": {
                "management_fee": self.management_fee_rate,
                "performance_fee": self.performance_fee_rate
            },
            "hurdle_rate": self.hurdle_rate
        }

    def update_nav(self, daily_return: float) -> float:
        """Updates Net Asset Value based on portfolio daily returns."""
        self.nav = self.nav * (1.0 + daily_return)
        self.aum = self.aum * (1.0 + daily_return)
        logger.info(f"Updated Fund NAV: ${self.nav:.2f}, AUM: ${self.aum:,.2f}")
        return self.nav
