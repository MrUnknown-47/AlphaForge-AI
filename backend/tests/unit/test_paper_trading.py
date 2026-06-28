import pytest
from app.modules.trading.paper_trading import PaperLedger, PaperExecutionEngine, RiskController

def test_paper_ledger_initialization():
    ledger = PaperLedger(50000.0)
    assert ledger.cash == 50000.0
    assert len(ledger.positions) == 0
    assert ledger.realized_pnl == 0.0

def test_risk_controls_pre_trade():
    ledger = PaperLedger(100000.0)
    risk = RiskController(ledger)
    prices = {"AAPL": 150.0}

    # Verify that a 50k trade exceeds the 10% position limit (10k)
    allowed = risk.verify_pre_trade_limits("AAPL", 333, 150.0, prices)
    assert allowed is False

    # Verify that a small trade of 5 shares (750.0) passes
    allowed_small = risk.verify_pre_trade_limits("AAPL", 5, 150.0, prices)
    assert allowed_small is True

def test_execution_engine_friction():
    ledger = PaperLedger(10000.0)
    engine = PaperExecutionEngine(ledger, friction_bps=10.0) # 10 bps friction (0.1%)
    
    # Executing a buy order of 10 shares of AAPL at 100.0 (total = 1000.0)
    # Friction cost = 1000.0 * 0.001 = 1.0
    success = engine.execute_order("AAPL", "LONG", 10, 100.0)
    assert success is True
    assert ledger.transaction_costs == 1.0
    assert ledger.cash == 8999.0
