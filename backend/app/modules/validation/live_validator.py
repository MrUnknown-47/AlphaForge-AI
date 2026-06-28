import logging
from typing import Dict, Any, List
from datetime import datetime
from app.modules.validation.performance_tracker import PerformanceTracker
from app.modules.validation.risk_tracker import RiskTracker
from app.modules.validation.execution_tracker import ExecutionTracker
from app.modules.validation.drift_tracker import DriftTracker
from app.modules.validation.scorecard_generator import ScorecardGenerator
from app.modules.broker.service import get_broker

logger = logging.getLogger("LiveValidator")

class LiveValidator:
    def __init__(self) -> None:
        self.performance = PerformanceTracker()
        self.risk = RiskTracker()
        self.execution = ExecutionTracker()
        self.drift = DriftTracker()
        self.scorecard = ScorecardGenerator()

    async def execute_validation_cycle(self, prices: Dict[str, float]) -> Dict[str, Any]:
        """Runs the validation tracker checks for the current hour."""
        logger.info("Executing live paper trading validation checks...")
        
        # Query portfolio stats from active broker
        broker = get_broker()
        account = await broker.get_account()
        positions = await broker.get_positions()
        
        portfolio_val = account["portfolio_value"]
        
        # Log dummy execution prices for universe tickers
        for pos in positions:
            ticker = pos["ticker"]
            expected = pos["entry_price"]
            fill = prices.get(ticker, expected)
            self.execution.log_execution(ticker, expected, fill, 12.5, 45.0)

        # Log simulated daily returns
        import random
        ret = random.uniform(-0.005, 0.008)
        pnl = portfolio_val * ret
        self.performance.add_daily_return(ret, pnl)
        self.risk.add_return(ret)
        
        # Log dummy predictions for drift audits
        self.drift.add_prediction(0.015, ret)

        # Evaluate performance statistics
        perf_metrics = self.performance.compute_rolling_metrics(30)
        risk_metrics = self.risk.analyze_risk_limits(
            portfolio_val, positions, pnl, perf_metrics["max_drawdown"]
        )
        drift_metrics = self.drift.compute_drift_metrics()
        exec_metrics = self.execution.get_average_metrics()

        # Generate scorecard
        sc = self.scorecard.generate_scorecard(
            paper_days=30,
            sharpe=perf_metrics["sharpe"],
            sortino=perf_metrics["sortino"],
            max_drawdown=perf_metrics["max_drawdown"],
            hit_ratio=perf_metrics["hit_ratio"],
            profit_factor=perf_metrics["profit_factor"],
            psi=drift_metrics["psi_drift"],
            latency_ms=exec_metrics["avg_latency_ms"],
            daily_loss=abs(pnl) / portfolio_val if portfolio_val > 0 else 0.0
        )

        return {
            "performance": perf_metrics,
            "risk": risk_metrics,
            "drift": drift_metrics,
            "scorecard": sc
        }
