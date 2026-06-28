import logging
from datetime import datetime
from typing import Dict, Any, List

logger = logging.getLogger("PositionReconciler")

class PositionReconciler:
    def __init__(self) -> None:
        pass

    def reconcile(
        self, local_cash: float, local_positions: Dict[str, Dict[str, float]],
        alpaca_cash: float, alpaca_positions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Compares local ledger state against broker endpoints to flag mismatches."""
        mismatches = []
        
        # Cash reconciliation (within 1 cent buffer)
        cash_diff = abs(local_cash - alpaca_cash)
        if cash_diff > 0.01:
            mismatches.append(f"CASH_MISMATCH: Local cash ${local_cash:.2f} vs Alpaca cash ${alpaca_cash:.2f}")

        # Map Alpaca list to dict
        a_pos_dict = {pos["ticker"]: pos for pos in alpaca_positions}

        # Check local positions against Alpaca positions
        for ticker, pos in local_positions.items():
            if ticker not in a_pos_dict:
                mismatches.append(f"POSITION_MISSING: {ticker} exists locally but not on Alpaca")
            else:
                a_pos = a_pos_dict[ticker]
                # Quantity mismatch check
                if abs(pos["quantity"] - a_pos["quantity"]) > 1e-4:
                    mismatches.append(f"QUANTITY_MISMATCH: {ticker} qty local {pos['quantity']} vs Alpaca {a_pos['quantity']}")
                # Average price mismatch check (within 1 cent buffer)
                if abs(pos["entry_price"] - a_pos["entry_price"]) > 0.01:
                    mismatches.append(f"PRICE_MISMATCH: {ticker} price local {pos['entry_price']} vs Alpaca {a_pos['entry_price']}")

        # Check for positions on Alpaca that do not exist locally
        for ticker in a_pos_dict:
            if ticker not in local_positions:
                mismatches.append(f"POSITION_EXTRA: {ticker} exists on Alpaca but not locally")

        ok = len(mismatches) == 0
        if not ok:
            logger.warning(f"Position reconciliation mismatch detected: {mismatches}")
            
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "reconciliation_ok": ok,
            "cash_diff": cash_diff,
            "position_mismatches": mismatches
        }
