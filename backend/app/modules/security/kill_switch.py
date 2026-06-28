import logging
from typing import Dict, Any

logger = logging.getLogger("KillSwitch")

class KillSwitch:
    def __init__(self) -> None:
        self.trading_enabled = True
        self.kill_switch_active = False

    def evaluate_state(self, conditions: Dict[str, Any]) -> bool:
        """
        Triggers global kill switch if:
        - drawdown > 20%
        - daily loss > 3%
        - broker offline
        - database offline
        - PSI > 0.25
        - Sharpe < 1.0
        - hit ratio < 55%
        - reconciliation failure
        """
        reasons = []

        if abs(conditions.get("drawdown", 0.0)) > 0.20:
            reasons.append("DRAWDOWN_BREACH")
        if abs(conditions.get("daily_loss_pct", 0.0)) > 0.03:
            reasons.append("DAILY_LOSS_BREACH")
        if not conditions.get("broker_online", True):
            reasons.append("BROKER_OFFLINE")
        if not conditions.get("db_online", True):
            reasons.append("DATABASE_OFFLINE")
        if conditions.get("psi", 0.0) > 0.25:
            reasons.append("PSI_DRIFT_BREACH")
        if conditions.get("sharpe", 1.5) < 1.0:
            reasons.append("SHARPE_COLLAPSE")
        if conditions.get("hit_ratio", 0.60) < 0.55:
            reasons.append("HIT_RATIO_COLLAPSE")
        if not conditions.get("reconciliation_ok", True):
            reasons.append("RECONCILIATION_FAILURE")

        if reasons:
            self.trading_enabled = False
            self.kill_switch_active = True
            logger.critical(f"GLOBAL KILL SWITCH ACTIVATED! Triggered reasons: {reasons}")
        
        return self.trading_enabled
