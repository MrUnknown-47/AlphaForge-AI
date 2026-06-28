import pytest
from app.modules.validation.live_validator import LiveValidator

@pytest.mark.asyncio
async def test_live_validator_cycle():
    validator = LiveValidator()
    prices = {"AAPL": 182.50}
    res = await validator.execute_validation_cycle(prices)
    
    assert "performance" in res
    assert "risk" in res
    assert "drift" in res
    assert "scorecard" in res
