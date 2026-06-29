import pytest
from app.modules.execution.execution_router import ExecutionRouter
from app.modules.execution.order_models import OrderRequest
from app.modules.execution.slippage_engine import SlippageEngine
from app.modules.execution.risk_checks import RiskChecks

@pytest.mark.asyncio
async def test_slippage_calculation():
    engine = SlippageEngine(base_spread_bps=2.0, market_impact_coef=0.1)
    
    # Verify spread applied correctly on Buy/Sell
    buy_price = engine.get_fill_price(base_price=100.0, side="BUY", quantity=100.0)
    sell_price = engine.get_fill_price(base_price=100.0, side="SELL", quantity=100.0)
    
    assert buy_price > 100.0
    assert sell_price < 100.0

@pytest.mark.asyncio
async def test_risk_checks_validation():
    checks = RiskChecks()
    
    # 1. Normal order size
    assert checks.validate_order("AAPL", quantity=100.0, current_leverage=1.5) is True

    # 2. Oversized order size
    assert checks.validate_order("AAPL", quantity=10000.0, current_leverage=1.5) is False

    # 3. Leverage limit violation
    assert checks.validate_order("AAPL", quantity=100.0, current_leverage=5.0) is False

    # 4. Emergency Kill Switch
    checks.set_kill_switch(True)
    assert checks.validate_order("AAPL", quantity=100.0, current_leverage=1.5) is False

@pytest.mark.asyncio
async def test_paper_engine_fills():
    router = ExecutionRouter()
    
    # Initialize mock cash balance
    assert router.paper.cash == 100000.0
    
    # Buy Order
    req = OrderRequest(ticker="AAPL", side="BUY", quantity=10.0, price=150.0)
    order = await router.route_order(req)
    assert order.status == "FILLED"
    assert order.price == 150.0
    
    # Verify position and account balance updates
    positions = router.paper.get_positions()
    assert len(positions) == 1
    assert positions[0].ticker == "AAPL"
    assert positions[0].quantity == 10.0
    
    account = router.paper.get_account()
    assert account.cash == 100000.0 - (150.0 * 10.0)
