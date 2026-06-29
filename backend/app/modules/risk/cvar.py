from typing import List
from app.modules.risk.var import calculate_historical_var

def calculate_cvar(returns: List[float], confidence: float = 0.95) -> float:
    if not returns:
        return 0.0
    var_val = calculate_historical_var(returns, confidence)
    tail_losses = [x for x in returns if x < -var_val]
    
    if not tail_losses:
        return var_val
    return abs(sum(tail_losses) / len(tail_losses))
