from typing import Dict, Any

class LedgerReconciliation:
    def compare_ledgers(self, internal_cash: float, broker_cash: float) -> Dict[str, Any]:
        variance = abs(internal_cash - broker_cash)
        
        if variance == 0.0:
            status = "MATCH"
        elif variance < 50.0:
            status = "WARNING"
        else:
            status = "BREAK"
            
        return {
            "status": status,
            "internal_cash": internal_cash,
            "broker_cash": broker_cash,
            "cash_variance": variance
        }
