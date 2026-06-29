from typing import Dict, Any

class RiskLimitsManager:
    def __init__(self, max_drawdown: float = 0.15) -> None:
        self.max_drawdown = max_drawdown
        self.kill_switch_active = False

    def evaluate_drawdown(self, current_drawdown: float) -> Dict[str, Any]:
        breached = current_drawdown > self.max_drawdown
        
        if breached:
            action = "LIQUIDATE"
            self.kill_switch_active = True
        elif current_drawdown > self.max_drawdown * 0.7:
            action = "REDUCE"
        else:
            action = "WARNING" if current_drawdown > self.max_drawdown * 0.5 else "NONE"
            
        return {
            "max_drawdown_limit": self.max_drawdown,
            "current_drawdown": current_drawdown,
            "limit_breached": breached,
            "action_required": action
        }
