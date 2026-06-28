import pytest
from app.modules.shadow_trading.position_reconciler import PositionReconciler

def test_position_reconciler_perfect():
    reconciler = PositionReconciler()
    local_pos = {"AAPL": {"quantity": 10.0, "entry_price": 180.0}}
    alpaca_pos = [{"ticker": "AAPL", "quantity": 10.0, "entry_price": 180.0}]
    
    res = reconciler.reconcile(1000.0, local_pos, 1000.0, alpaca_pos)
    assert res["reconciliation_ok"] is True
    assert len(res["position_mismatches"]) == 0

def test_position_reconciler_mismatches():
    reconciler = PositionReconciler()
    local_pos = {"AAPL": {"quantity": 10.0, "entry_price": 180.0}}
    alpaca_pos = [{"ticker": "AAPL", "quantity": 12.0, "entry_price": 180.0}] # mismatch quantity
    
    res = reconciler.reconcile(1000.0, local_pos, 950.0, alpaca_pos) # mismatch cash too
    assert res["reconciliation_ok"] is False
    assert len(res["position_mismatches"]) == 2
