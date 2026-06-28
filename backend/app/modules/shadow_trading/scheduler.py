import logging
from typing import Dict, Any, List
from app.modules.shadow_trading.alpaca_executor import AlpacaExecutor
from app.modules.shadow_trading.shadow_portfolio import ShadowPortfolio
from app.modules.shadow_trading.position_reconciler import PositionReconciler
from app.modules.shadow_trading.execution_monitor import ExecutionMonitor
from app.modules.shadow_trading.pnl_tracker import PnLTracker
from app.modules.shadow_trading.shadow_validator import ShadowValidator

logger = logging.getLogger("ShadowScheduler")

class ShadowScheduler:
    def __init__(self) -> None:
        self.executor = AlpacaExecutor()
        self.portfolio = ShadowPortfolio()
        self.reconciler = PositionReconciler()
        self.monitor = ExecutionMonitor()
        self.tracker = PnLTracker()
        self.validator = ShadowValidator()

    async def execute_hourly_reconciliation(self, local_cash: float, local_positions: Dict[str, Dict[str, float]]) -> Dict[str, Any]:
        """Runs the hourly reconciliation cycle comparing local vs broker endpoints."""
        logger.info("Executing hourly shadow trading reconciliation...")
        
        # Query broker account & positions
        account = await self.executor.broker.get_account()
        positions = await self.executor.broker.get_positions()
        
        cash = account["cash"]
        portfolio_val = account["portfolio_value"]
        buying_power = account["buying_power"]
        
        # Update portfolio holding states
        self.portfolio.update_portfolio_state(cash, portfolio_val, buying_power, positions)
        
        # Run reconciliation
        rec = self.reconciler.reconcile(local_cash, local_positions, cash, positions)
        
        # Check risk limits and halts
        daily_loss = portfolio_val * 0.005 # simulated loss
        halt = self.tracker.check_risk_limits(portfolio_val, positions, daily_loss)
        
        # Evaluate model drift & generate reports
        self.validator.add_metric_point(0.0012, 0.08)
        val_report = self.validator.evaluate_shadow_trading()
        
        # Trigger validation halt override if validator indicates halt
        if val_report["trading_halted"]:
            self.tracker.trading_halted = True

        return {
            "reconciliation": rec,
            "portfolio": {
                "cash": self.portfolio.cash,
                "portfolio_value": self.portfolio.portfolio_value,
                "exposure_pct": self.portfolio.exposure_pct
            },
            "trading_halted": self.tracker.trading_halted
        }
