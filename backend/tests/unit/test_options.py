import pytest
from app.modules.derivatives.strategies.service import OptionsStrategyService

def test_covered_call():
    res = OptionsStrategyService.covered_call(100.0, 105.0, 3.0)
    assert res["strategy"] == "Covered Call"
    assert res["max_profit"] == 8.0
    assert res["max_loss"] == 97.0
    assert res["breakeven"] == [97.0]

def test_iron_condor():
    res = OptionsStrategyService.iron_condor(100.0, 95.0, 90.0, 105.0, 110.0, 2.0)
    assert res["strategy"] == "Iron Condor"
    assert res["max_profit"] == 2.0
    assert res["max_loss"] == 3.0
    assert res["breakeven"] == [93.0, 107.0]
