from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from datetime import datetime

from app.shared.database import get_db
from app.modules.research.factors import FactorEngine
from app.modules.research.validation import run_adf_test, run_kpss_test, run_jarque_bera, calculate_hurst_exponent
from app.modules.research.regime import RegimeDetector
from app.modules.research.correlation import calculate_pearson, calculate_spearman
from app.modules.research.clustering import AssetClusteredEngine
from app.modules.research.explainability import ModelExplainability
from app.modules.research.schemas import (
    ResearchFactorResponse,
    FeatureExplorerResponse,
    StatValidationResponse,
    RegimeResponse,
    CorrelationResponse,
    ClusterResponse,
    ExplainabilityResponse
)

router = APIRouter(prefix="/research", tags=["Research & Validation Engine"])

factor_engine = FactorEngine()
regime_detector = RegimeDetector()
cluster_engine = AssetClusteredEngine()
explain_engine = ModelExplainability()

@router.get("/factors", response_model=List[ResearchFactorResponse])
async def get_factors(symbol: str = "SPY"):
    # Mock prices for exposures check
    prices = [150.0, 151.0, 149.0, 152.0, 155.0]
    exposures = factor_engine.calculate_exposures(symbol, prices)
    returns = factor_engine.calculate_factor_returns()
    
    return [
        {
            "name": f,
            "factor_returns": returns.get(f, []),
            "exposures": {symbol: exposures.get(f, 0.0)}
        }
        for f in factor_engine.factors
    ]

@router.get("/features", response_model=List[FeatureExplorerResponse])
async def get_features():
    return [
        {"name": "returns_1d", "feature_type": "technical", "importance": 0.35},
        {"name": "volatility_30d", "feature_type": "volatility", "importance": 0.28},
        {"name": "pe_ratio", "feature_type": "fundamental", "importance": 0.15}
    ]

@router.get("/validation", response_model=List[StatValidationResponse])
async def get_validation(symbol: str = "SPY"):
    prices = [150.0, 151.0, 149.0, 152.0, 155.0]
    returns = [0.006, -0.013, 0.02, 0.019]
    
    adf = run_adf_test(prices)
    kpss = run_kpss_test(prices)
    jb = run_jarque_bera(returns)
    
    return [
        {"test_name": "ADF", "statistic": adf["statistic"], "p_value": adf["p_value"], "passed": adf["passed"]},
        {"test_name": "KPSS", "statistic": kpss["statistic"], "p_value": kpss["p_value"], "passed": kpss["passed"]},
        {"test_name": "Jarque-Bera", "statistic": jb["statistic"], "p_value": jb["p_value"], "passed": jb["passed"]}
    ]

@router.get("/regimes", response_model=RegimeResponse)
async def get_regimes(symbol: str = "SPY"):
    prices = [150.0, 151.0, 149.0, 152.0, 155.0]
    res = regime_detector.detect_regime(prices)
    
    return {
        "timestamp": datetime.utcnow(),
        "regime_name": res["regime"],
        "probability": res["probability"]
    }

@router.get("/correlation", response_model=CorrelationResponse)
async def get_correlation(symbol_a: str = "AAPL", symbol_b: str = "MSFT"):
    returns_a = [0.01, -0.015, 0.02, 0.005]
    returns_b = [0.012, -0.011, 0.018, 0.002]
    
    pearson = calculate_pearson(returns_a, returns_b)
    spearman = calculate_spearman(returns_a, returns_b)
    
    return {
        "symbol_a": symbol_a,
        "symbol_b": symbol_b,
        "pearson": pearson,
        "spearman": spearman
    }

@router.get("/clusters", response_model=List[ClusterResponse])
async def get_clusters():
    symbols = ["AAPL", "MSFT", "TSLA", "NVDA", "SPY", "QQQ"]
    clusters = cluster_engine.cluster_assets(symbols)
    return [
        {"cluster_id": c["cluster_id"], "members": c["members"]}
        for c in clusters
    ]

@router.get("/explainability", response_model=List[ExplainabilityResponse])
async def get_explainability():
    values = explain_engine.get_shap_values()
    return [
        {"feature_name": v["feature_name"], "shap_value": v["shap_value"]}
        for v in values
    ]

@router.get("/optimization")
async def get_optimization():
    return {
        "status": "success",
        "optimal_weights": {"AAPL": 0.4, "MSFT": 0.4, "TSLA": 0.2}
    }

@router.post("/analyze")
async def analyze_data(symbol: str):
    return {"status": "analyzed", "symbol": symbol, "timestamp": datetime.utcnow()}
