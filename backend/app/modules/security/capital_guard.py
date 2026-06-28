from typing import Dict, Any

class CapitalGuard:
    def __init__(self) -> None:
        self.max_single_order = 500.0
        self.max_position = 1000.0
        self.max_daily_loss = 100.0
        self.max_total_loss = 500.0
        self.max_portfolio_exposure = 0.50

    def validate_order(self, order_value: float, current_position_value: float, current_exposure: float) -> Dict[str, Any]:
        """
        Validates order size against capital guardrails:
        - Checks single order size limit ($500)
        - Checks maximum position limit ($1000)
        - Checks portfolio exposure limits (50%)
        """
        allowed = True
        reason = ""
        require_confirmation = False

        if order_value > self.max_single_order:
            allowed = False
            reason = "ORDER_SIZE_LIMIT_BREACHED"
        if order_value > 500.0:
            require_confirmation = True

        if current_position_value + order_value > self.max_position:
            allowed = False
            reason = "POSITION_LIMIT_BREACHED"

        if current_exposure > self.max_portfolio_exposure:
            allowed = False
            reason = "EXPOSURE_LIMIT_BREACHED"

        return {
            "allowed": allowed,
            "reason": reason,
            "requires_manual_confirmation": require_confirmation
        }
