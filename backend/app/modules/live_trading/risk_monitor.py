import logging
from typing import Dict, List, Any

logger = logging.getLogger("LiveRiskMonitor")

class LiveRiskMonitor:
    def __init__(self) -> None:
        self.max_position_pct = 0.10
        self.max_portfolio_exposure = 0.50
        self.max_daily_loss = 0.03
        self.max_drawdown = 0.20
        self.daily_high = 0.0
        self.initial_value = 0.0

    def check_pre_trade_limits(
        self, ticker: str, quantity: float, price: float, portfolio_val: float, active_positions: List[Dict[str, Any]]
    ) -> bool:
        trade_val = quantity * price
        
        # 1. Max Position size check (10%)
        if trade_val > portfolio_val * self.max_position_pct:
            logger.warning(f"Risk Reject: Position size {trade_val:.2f} exceeds 10% limit ({portfolio_val * self.max_position_pct:.2f})")
            return False

        # 2. Max Portfolio Exposure check (50%)
        active_exposure = 0.0
        for pos in active_positions:
            active_exposure += abs(pos["quantity"]) * pos["entry_price"]
            
        if active_exposure + trade_val > portfolio_val * self.max_portfolio_exposure:
            logger.warning(f"Risk Reject: Total exposure {active_exposure + trade_val:.2f} exceeds 50% limit ({portfolio_val * self.max_portfolio_exposure:.2f})")
            return False

        return True

    def check_post_trade_limits(self, portfolio_val: float) -> List[str]:
        alerts = []
        if self.initial_value == 0.0:
            self.initial_value = portfolio_val
            self.daily_high = portfolio_val

        if portfolio_val > self.daily_high:
            self.daily_high = portfolio_val

        # Drawdown limit (20%)
        drawdown = (portfolio_val - self.daily_high) / self.daily_high
        if abs(drawdown) > self.max_drawdown:
            alerts.append(f"ALERT: Max Drawdown breached! Current: {drawdown*100:.2f}% (Limit: 20%)")

        # Daily loss limit (3%)
        daily_change = (portfolio_val - self.initial_value) / self.initial_value
        if daily_change < -self.max_daily_loss:
            alerts.append(f"ALERT: Max Daily Loss breached! Change: {daily_change*100:.2f}% (Limit: -3%)")

        return alerts
