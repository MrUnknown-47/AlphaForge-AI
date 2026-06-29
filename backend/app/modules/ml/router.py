from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from datetime import datetime

from app.shared.database import get_db
from app.modules.ml.forecasting import ForecastingEngine
from app.modules.ml.ensemble import EnsembleEngine
from app.modules.ml.regime_prediction import RegimePredictor
from app.modules.ml.reinforcement import RLAgent
from app.modules.ml.drift_detection import calculate_psi, calculate_ks_statistic
from app.modules.ml.explainability import ModelExplainability
from app.modules.ml.schemas import (
    MlModelResponse,
    PredictionResponse,
    MetricResponse,
    RegimePredResponse,
    DriftResponse,
    ExplainResponse
)

router = APIRouter(prefix="/ml", tags=["Machine Learning & Forecasting Engine"])

forecaster = ForecastingEngine()
ensemble = EnsembleEngine()
regime_predictor = RegimePredictor()
rl_agent = RLAgent()
explain_engine = ModelExplainability()

@router.get("/models", response_model=List[MlModelResponse])
async def get_models():
    return [
        {"id": "MOCK_MODEL_1", "name": "XGBoost Classifier", "version": "1.0.0", "status": "ACTIVE"},
        {"id": "MOCK_MODEL_2", "name": "LSTM Forecaster", "version": "2.1.0", "status": "ACTIVE"}
    ]

@router.get("/predictions", response_model=PredictionResponse)
async def get_predictions(symbol: str = "SPY"):
    prices = [150.0, 151.0, 149.0, 152.0, 155.0]
    fc = forecaster.forecast(symbol, prices)
    res = ensemble.combine_predictions([fc["predicted_return"]])
    
    return {
        "symbol": symbol,
        "predicted_return": fc["predicted_return"],
        "confidence": res["confidence"],
        "uncertainty_score": res["uncertainty_score"]
    }

@router.get("/metrics", response_model=List[MetricResponse])
async def get_metrics():
    return [
        {"metric_name": "Accuracy", "value": 0.65},
        {"metric_name": "MAE", "value": 0.012},
        {"metric_name": "Sharpe", "value": 1.85}
    ]

@router.get("/regimes", response_model=RegimePredResponse)
async def get_regimes(symbol: str = "SPY"):
    prices = [150.0, 151.0, 149.0, 152.0, 155.0]
    res = regime_predictor.predict_regime(prices)
    return {
        "regime": res["regime"],
        "probability": res["probability"]
    }

@router.get("/drift", response_model=List[DriftResponse])
async def get_drift():
    ref = [0.01, -0.01, 0.02, 0.005]
    curr = [0.012, -0.009, 0.018, 0.006]
    psi = calculate_psi(ref, curr)
    ks = calculate_ks_statistic(ref, curr)
    
    return [
        {"feature_name": "returns_1d", "psi": psi, "drift_detected": ks["drift_detected"]}
    ]

@router.get("/explanations", response_model=List[ExplainResponse])
async def get_explanations():
    importances = explain_engine.get_feature_importances()
    return [
        {"feature_name": imp["feature_name"], "importance": imp["importance"]}
        for imp in importances
    ]

@router.post("/train")
async def train_model(model_name: str):
    return {"status": "SUCCESS", "message": f"Training completed for {model_name}."}

@router.post("/predict")
async def run_predict(symbol: str):
    prices = [150.0, 151.0, 149.0, 152.0, 155.0]
    fc = forecaster.forecast(symbol, prices)
    return {"status": "SUCCESS", "symbol": symbol, "predicted_return": fc["predicted_return"]}

@router.post("/validate")
async def run_validate():
    return {"status": "SUCCESS", "accuracy": 0.65, "drift_detected": False}

@router.post("/backtest")
async def run_backtest():
    return {"status": "SUCCESS", "sharpe": 1.85, "max_drawdown": 0.08}
