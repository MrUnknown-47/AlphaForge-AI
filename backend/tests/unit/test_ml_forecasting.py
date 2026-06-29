import pytest
from app.modules.ml.forecasting import ForecastingEngine
from app.modules.ml.ensemble import EnsembleEngine
from app.modules.ml.regime_prediction import RegimePredictor
from app.modules.ml.reinforcement import RLAgent
from app.modules.ml.drift_detection import calculate_psi, calculate_ks_statistic

@pytest.mark.asyncio
async def test_forecasting():
    engine = ForecastingEngine()
    prices = [100.0, 101.0, 99.0, 102.0, 105.0]
    res = engine.forecast("SPY", prices)
    
    assert res["predicted_return"] > 0.0
    assert res["predicted_volatility"] == 0.15
    assert res["predicted_drawdown"] == 0.08

@pytest.mark.asyncio
async def test_ensemble_combination():
    engine = EnsembleEngine()
    res = engine.combine_predictions([0.05, 0.07, 0.06])
    
    assert res["prediction"] == pytest.approx(0.06)
    assert res["confidence"] == 0.88
    assert res["uncertainty_score"] == 0.05

@pytest.mark.asyncio
async def test_regime_predictions():
    pred = RegimePredictor()
    prices_bull = [100.0, 102.0, 105.0, 107.0, 110.0]
    res = pred.predict_regime(prices_bull)
    assert res["regime"] == "BULL"

@pytest.mark.asyncio
async def test_rl_policy_decisions():
    agent = RLAgent()
    
    # 1. Buy check
    state_buy = {"sharpe": 1.8, "drawdown": 0.02}
    assert agent.get_action(state_buy) == "BUY"

    # 2. Hedge check
    state_hedge = {"sharpe": 0.5, "drawdown": 0.18}
    assert agent.get_action(state_hedge) == "HEDGE"

@pytest.mark.asyncio
async def test_drift_and_ks_statistics():
    ref = [0.01, -0.01, 0.02, 0.005]
    curr = [0.012, -0.009, 0.018, 0.006]
    
    psi = calculate_psi(ref, curr)
    assert psi == 0.085
    
    ks = calculate_ks_statistic(ref, curr)
    assert ks["drift_detected"] is False
