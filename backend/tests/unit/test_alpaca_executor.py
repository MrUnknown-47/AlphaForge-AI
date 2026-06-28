import pytest
from app.modules.shadow_trading.alpaca_executor import AlpacaExecutor

@pytest.mark.asyncio
async def test_alpaca_executor_trading():
    executor = AlpacaExecutor()
    res = await executor.execute_trade("AAPL", "BUY", 10, type="MARKET")
    assert res["ticker"] == "AAPL"
    assert res["status"] in ["FILLED", "PENDING"]
