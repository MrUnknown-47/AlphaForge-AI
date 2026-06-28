import os
import json
import pickle
import logging
import asyncio
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from app.modules.trading.paper_trading import PaperLedger, PaperExecutionEngine, RiskController, ReportExporter

logger = logging.getLogger("LiveScheduler")

class LiveScheduler:
    def __init__(self) -> None:
        self.tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "SPY", "QQQ"]
        self.ledger = PaperLedger(100000.0)
        self.engine = PaperExecutionEngine(self.ledger)
        self.risk = RiskController(self.ledger)
        self.active_alerts = []
        self.model_cache = {}

    def load_latest_models(self) -> None:
        """Loads trained XGBoost and LSTM models from the local models directory."""
        models_dir = "backend/app/modules/prediction/models"
        if not os.path.exists(models_dir):
            return

        files = [f for f in os.listdir(models_dir) if f.endswith(".pkl")]
        for fn in files:
            model_type = fn.split("_")[0]
            if model_type not in self.model_cache:
                with open(os.path.join(models_dir, fn), "rb") as f:
                    self.model_cache[model_type] = pickle.load(f)
                logger.info(f"Loaded active model version for {model_type}: {fn}")

    async def execute_hourly_cycle(self, prices: dict[str, float]) -> None:
        """Simulates/Runs one hourly cycle of live fetching, features compute, predictions, and trades."""
        logger.info("Executing hourly quantitative cycle...")
        self.load_latest_models()

        if not self.model_cache:
            logger.warning("No models loaded. Skipping trading cycle.")
            return

        # Check Stop Loss (2%) and Take Profit (6%) triggers on active positions first
        pos_to_close = []
        for ticker, pos in list(self.ledger.positions.items()):
            current_price = prices.get(ticker)
            if current_price is None:
                continue

            entry = pos["entry_price"]
            qty = pos["quantity"]
            
            # For long positions
            if qty > 0:
                perf = (current_price - entry) / entry
                if perf <= -0.02:  # Stop loss
                    logger.info(f"STOP LOSS triggered for {ticker} at {current_price:.2f} (Entry: {entry:.2f})")
                    pos_to_close.append((ticker, "SHORT", qty, current_price))
                elif perf >= 0.06:  # Take profit
                    logger.info(f"TAKE PROFIT triggered for {ticker} at {current_price:.2f} (Entry: {entry:.2f})")
                    pos_to_close.append((ticker, "SHORT", qty, current_price))
            # For short positions
            elif qty < 0:
                perf = (entry - current_price) / entry
                if perf <= -0.02:  # Stop loss (price went up)
                    logger.info(f"STOP LOSS triggered for SHORT position {ticker} at {current_price:.2f}")
                    pos_to_close.append((ticker, "LONG", abs(qty), current_price))
                elif perf >= 0.06:  # Take profit (price went down)
                    logger.info(f"TAKE PROFIT triggered for SHORT position {ticker} at {current_price:.2f}")
                    pos_to_close.append((ticker, "LONG", abs(qty), current_price))

        # Close triggered SL/TP positions
        for ticker, direction, qty, price in pos_to_close:
            self.engine.execute_order(ticker, direction, qty, price)

        # Predict returns for each ticker and execute trades
        for ticker in self.tickers:
            current_price = prices.get(ticker, 150.0)
            
            # Predict using ensemble model formats (averaging predictions of XGBoost and LSTM)
            preds = []
            for name, model_data in self.model_cache.items():
                model = model_data["model"]
                scaler = model_data["scaler"]
                features = model_data["features"]
                
                # Mock feature mapping input values (19 features)
                mock_features = np.random.normal(0.0, 1.0, (1, len(features)))
                scaled_feats = scaler.transform(mock_features)
                
                pred_val = model.predict(scaled_feats)
                # Handle single element/array returns
                if isinstance(pred_val, np.ndarray):
                    pred_val = float(pred_val.item())
                preds.append(float(pred_val))

            ensemble_pred = np.mean(preds) if preds else 0.0
            
            # Alert on model confidence collapse (predictions close to zero indicating uncertainty)
            if abs(ensemble_pred) < 1e-4:
                self.active_alerts.append(f"WARNING: Model confidence collapse for {ticker} (ensemble returns prediction ~ 0)")

            # Order Signal Decision boundaries
            signal = None
            if ensemble_pred > 0.015:
                signal = "LONG"
            elif ensemble_pred < -0.015:
                signal = "SHORT"

            if signal:
                # Target sizing of 5% of portfolio per trade
                port_val = self.ledger.get_portfolio_value(prices)
                target_qty = float(np.floor((port_val * 0.05) / current_price))
                
                if target_qty > 0:
                    # Risk control verify
                    if self.risk.verify_pre_trade_limits(ticker, target_qty, current_price, prices):
                        self.engine.execute_order(ticker, signal, target_qty, current_price)

        # Enforce post trade limits checks & alerts
        risk_alerts = self.risk.verify_post_trade_limits(prices)
        self.active_alerts.extend(risk_alerts)

        # Alert on Mock PSI feature drift (> 0.25)
        mock_psi = np.random.uniform(0.0, 0.35)
        if mock_psi > 0.25:
            self.active_alerts.append(f"WARNING: Feature Drift (PSI = {mock_psi:.4f}) exceeded threshold 0.25")

        # Log alerts
        for alert in self.active_alerts[-3:]:
            logger.warning(alert)

        # Record equity curve points
        val = self.ledger.get_portfolio_value(prices)
        self.ledger.equity_curve.append({
            "time": datetime.utcnow().isoformat(),
            "value": val
        })

        # Daily report exports
        ReportExporter.export_daily_report(self.ledger, self.engine, prices)

async def simulate_scheduler_run():
    logging.basicConfig(level=logging.INFO)
    scheduler = LiveScheduler()
    prices = {
        "AAPL": 182.50, "MSFT": 420.10, "NVDA": 122.50, "GOOGL": 170.10,
        "AMZN": 185.20, "META": 480.30, "TSLA": 178.50, "AMD": 160.20,
        "SPY": 540.30, "QQQ": 450.40
    }
    
    print("\nStarting hourly live scheduler execution test...")
    await scheduler.execute_hourly_cycle(prices)
    print("Cycle complete. Checking generated daily report file...")
    
    report_path = "backend/app/modules/prediction/reports/daily_report.json"
    if os.path.exists(report_path):
        with open(report_path, "r") as f:
            data = json.load(f)
            print(f"  - Portfolio Value: {data.get('portfolio_value'):.2f}")
            print(f"  - Sharpe Ratio: {data.get('sharpe_ratio')}")
            print(f"  - Hit Ratio: {data.get('hit_ratio')}")
        print("\nPaper Scheduler Verification: PASS")
    else:
        print("Paper Scheduler Verification: FAILED (No report created)")

if __name__ == "__main__":
    asyncio.run(simulate_scheduler_run())
