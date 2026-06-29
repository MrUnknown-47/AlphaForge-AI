import pytest
from app.modules.shadow.shadow_engine import ShadowTradingEngine
from app.modules.shadow.reconciliation import LedgerReconciliation

@pytest.mark.asyncio
async def test_shadow_mirror_exec():
    engine = ShadowTradingEngine()
    res = engine.mirror_order("SPY", "BUY", 100)
    
    assert res["symbol"] == "SPY"
    assert res["expected_fill_price"] == 150.25
    assert res["actual_fill_price"] == 150.28
    assert res["slippage_bps"] == pytest.approx(1.99667, rel=1e-4)

@pytest.mark.asyncio
async def test_ledger_matching():
    reconciler = LedgerReconciliation()
    
    # 1. Perfect match
    res_match = reconciler.compare_ledgers(50000.0, 50000.0)
    assert res_match["status"] == "MATCH"
    
    # 2. Warning variance
    res_warn = reconciler.compare_ledgers(50000.0, 50020.0)
    assert res_warn["status"] == "WARNING"

    # 3. Break variance
    res_break = reconciler.compare_ledgers(50000.0, 50100.0)
    assert res_break["status"] == "BREAK"
