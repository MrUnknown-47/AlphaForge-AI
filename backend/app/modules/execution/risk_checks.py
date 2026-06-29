class RiskChecks:
    def __init__(self) -> None:
        self.kill_switch_active = False
        self.max_position_size = 10000.0  # shares
        self.max_order_size = 5000.0      # shares
        self.max_leverage = 4.0

    def set_kill_switch(self, active: bool) -> None:
        self.kill_switch_active = active

    def validate_order(self, ticker: str, quantity: float, current_leverage: float) -> bool:
        if self.kill_switch_active:
            return False
        if quantity > self.max_order_size:
            return False
        if current_leverage > self.max_leverage:
            return False
        return True
