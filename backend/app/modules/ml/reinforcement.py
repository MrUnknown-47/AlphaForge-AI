from typing import List, Dict, Any

class RLAgent:
    def get_action(self, state: Dict[str, Any]) -> str:
        # Action space: BUY, SELL, HOLD, REDUCE, HEDGE
        sharpe = state.get("sharpe", 0.0)
        drawdown = state.get("drawdown", 0.0)
        
        if sharpe > 1.5 and drawdown < 0.05:
            return "BUY"
        elif drawdown > 0.15:
            return "HEDGE"
        else:
            return "HOLD"
