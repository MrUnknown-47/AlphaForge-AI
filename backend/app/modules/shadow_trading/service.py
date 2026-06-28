from typing import Dict, Any, List
from app.modules.shadow_trading.scheduler import ShadowScheduler

# Cached instance singleton
_shadow_scheduler_instance = None

def get_shadow_scheduler() -> ShadowScheduler:
    global _shadow_scheduler_instance
    if _shadow_scheduler_instance is None:
        _shadow_scheduler_instance = ShadowScheduler()
    return _shadow_scheduler_instance

class ShadowTradingService:
    def __init__(self) -> None:
        self.scheduler = get_shadow_scheduler()

    async def run_reconciliation_cycle(self) -> Dict[str, Any]:
        return await self.scheduler.execute_hourly_reconciliation(100000.0, {})

    def get_account_summary(self) -> Dict[str, Any]:
        return {
            "cash": self.scheduler.portfolio.cash,
            "portfolio_value": self.scheduler.portfolio.portfolio_value,
            "buying_power": self.scheduler.portfolio.buying_power,
            "exposure_pct": self.scheduler.portfolio.exposure_pct,
            "trading_halted": self.scheduler.tracker.trading_halted
        }

    def get_positions(self) -> List[Dict[str, Any]]:
        pos_list = []
        for ticker, pos in self.scheduler.portfolio.positions.items():
            pos_list.append({
                "ticker": ticker,
                "quantity": pos["quantity"],
                "entry_price": pos["entry_price"],
                "market_value": pos["market_value"],
                "unrealized_pnl": pos["unrealized_pnl"]
            })
        return pos_list

    def get_performance_stats(self) -> Dict[str, Any]:
        return self.scheduler.validator.evaluate_shadow_trading()

    def get_execution_metrics(self) -> Dict[str, Any]:
        return self.scheduler.monitor.get_summary_stats()
