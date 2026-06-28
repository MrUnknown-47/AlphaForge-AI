import pytest
from app.modules.broker.service import get_broker
from app.modules.broker.paper_broker import PaperBroker
from app.modules.broker.alpaca_broker import AlpacaBroker
from app.config import settings

@pytest.mark.asyncio
async def test_broker_factory_routing():
    # Test PAPER default fallback routing
    settings.BROKER = "PAPER"
    broker_p = get_broker()
    assert isinstance(broker_p, PaperBroker)

@pytest.mark.asyncio
async def test_paper_broker_order_placement_and_balance():
    broker = PaperBroker()
    acc_before = await broker.get_account()
    initial_cash = acc_before["cash"]

    # Place LONG order for 10 shares of AAPL at 180.0 (total = 1800.0)
    # Friction cost = 1800.0 * 0.0005 = 0.90
    res = await broker.place_order("AAPL", "BUY", 10, price=180.0)
    assert res["status"] == "FILLED"

    acc_after = await broker.get_account()
    # Cash should be initial_cash - 1800.0 - 0.90 = initial_cash - 1800.90
    expected_cash = initial_cash - 1800.90
    assert abs(acc_after["cash"] - expected_cash) < 1e-4

@pytest.mark.asyncio
async def test_paper_broker_positions_and_sl_tp():
    broker = PaperBroker()
    # Add initial LONG position
    await broker.place_order("NVDA", "BUY", 10, price=100.0)
    
    positions = await broker.get_positions()
    assert len(positions) == 1
    assert positions[0]["ticker"] == "NVDA"
    assert positions[0]["quantity"] == 10.0
    assert positions[0]["entry_price"] == 100.0

    # Stop Loss Check (Trigger manual close at SL target: current price <= 98.0)
    current_price_sl = 97.50
    entry = positions[0]["entry_price"]
    perf = (current_price_sl - entry) / entry
    
    # Assert performance triggers SL (< -2%)
    assert perf <= -0.02
    
    # Close out position using close_position
    close_res = await broker.close_position("NVDA")
    assert close_res["status"] == "FILLED"
    
    positions_after = await broker.get_positions()
    assert len(positions_after) == 0
