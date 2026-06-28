import pytest
import pandas as pd
from app.modules.live_trading.stream import MarketStream
from app.modules.live_trading.feature_generator import FeatureGenerator
from app.modules.live_trading.model_loader import ModelLoader
from app.modules.live_trading.signal_engine import SignalEngine
from app.modules.live_trading.risk_monitor import LiveRiskMonitor
from app.modules.live_trading.scheduler import LiveScheduler

@pytest.mark.asyncio
async def test_live_stream_fallback():
    stream = MarketStream(["AAPL", "MSFT"])
    prices = await stream.fetch_yahoo_finance_fallback()
    assert "AAPL" in prices
    assert "MSFT" in prices
    assert prices["AAPL"] > 0.0

def test_feature_generator_count():
    fg = FeatureGenerator()
    # Create fake history dataframe
    history_records = []
    for i in range(50):
        history_records.append({
            "close": 150.0 + i,
            "high": 152.0 + i,
            "low": 149.0 + i,
            "open": 150.0 + i,
            "volume": 5000.0,
            "spy_close": 500.0 + i,
            "qqq_close": 440.0 + i,
            "pe": 20.0, "pb": 3.0, "roe": 0.15, "debt_to_equity": 0.5,
            "sentiment_mean": 0.1
        })
    df = pd.DataFrame(history_records)
    feats = fg.compute_features(df)
    
    assert len(feats) == 50
    # Assert all 19 features exist
    for col in fg.approved_features:
        assert col in feats.columns

@pytest.mark.asyncio
async def test_live_scheduler_run_cycle():
    # Execute full cycle test
    scheduler = LiveScheduler()
    await scheduler.execute_hourly_cycle()
    
    # Assert cycle stored predictions and signals
    assert len(scheduler.predictions_store) > 0
    assert len(scheduler.signals_store) > 0
    
    # Assert risk checks parameters are active
    assert scheduler.risk.max_position_pct == 0.10
    assert scheduler.risk.max_daily_loss == 0.03
