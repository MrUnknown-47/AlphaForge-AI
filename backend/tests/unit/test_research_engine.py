import pytest
from app.modules.research.factors import FactorEngine
from app.modules.research.validation import run_adf_test, run_kpss_test, run_jarque_bera, calculate_hurst_exponent
from app.modules.research.regime import RegimeDetector
from app.modules.research.correlation import calculate_pearson
from app.modules.research.clustering import AssetClusteredEngine
from app.modules.research.explainability import ModelExplainability

@pytest.mark.asyncio
async def test_factor_engine():
    engine = FactorEngine()
    
    # 1. Calculates Exposures
    prices = [100.0, 101.0, 99.0, 102.0, 105.0]
    exposures = engine.calculate_exposures("SPY", prices)
    assert exposures["Momentum"] > 0.0
    assert exposures["Value"] == 0.45

@pytest.mark.asyncio
async def test_statistical_validations():
    prices = [100.0, 101.0, 99.0, 102.0, 105.0]
    returns = [0.01, -0.02, 0.03, 0.029]
    
    adf = run_adf_test(prices)
    assert adf["passed"] is True
    
    kpss = run_kpss_test(prices)
    assert kpss["passed"] is True
    
    jb = run_jarque_bera(returns)
    assert jb["passed"] is True
    
    hurst = calculate_hurst_exponent(prices)
    assert hurst == 0.52

@pytest.mark.asyncio
async def test_regime_detection():
    detector = RegimeDetector()
    
    # Bull regime test
    prices_bull = [100.0, 102.0, 105.0, 107.0, 110.0] # +10% return
    res_bull = detector.detect_regime(prices_bull)
    assert res_bull["regime"] == "BULL"

    # Bear regime test
    prices_bear = [100.0, 98.0, 95.0, 93.0, 90.0] # -10% return
    res_bear = detector.detect_regime(prices_bear)
    assert res_bear["regime"] == "BEAR"

@pytest.mark.asyncio
async def test_correlation_and_clustering():
    returns_a = [0.01, -0.015, 0.02, 0.005]
    returns_b = [0.01, -0.015, 0.02, 0.005]
    
    # Pearson of identical series is 1.0
    pearson = calculate_pearson(returns_a, returns_b)
    assert pearson == pytest.approx(1.0)
    
    cluster_engine = AssetClusteredEngine()
    clusters = cluster_engine.cluster_assets(["AAPL", "MSFT"])
    assert len(clusters) > 0

@pytest.mark.asyncio
async def test_model_explainability():
    explain = ModelExplainability()
    shap_vals = explain.get_shap_values()
    assert len(shap_vals) > 0
    assert shap_vals[0]["feature_name"] == "Momentum_10d"
