import pytest
from app.modules.copilot.llm_provider import LLMProvider
from app.modules.copilot.regime_detector import RegimeDetector

@pytest.mark.asyncio
async def test_regime_detector_rules():
    provider = LLMProvider()
    detector = RegimeDetector(provider)
    corrs = {"AAPL-SPY": 0.75}
    
    # Test Bull Regime (Low Volatility)
    res_bull = await detector.detect_regime(12.0, 0.10, corrs)
    assert res_bull.current_regime == "BULL"
    assert res_bull.volatility_state == "LOW_VOLATILITY"
    assert res_bull.systemic_risk == "RISK_ON"

    # Test Bear Regime (High Volatility)
    res_bear = await detector.detect_regime(35.0, 0.40, corrs)
    assert res_bear.current_regime == "BEAR"
    assert res_bear.volatility_state == "HIGH_VOLATILITY"
    assert res_bear.systemic_risk == "RISK_OFF"
