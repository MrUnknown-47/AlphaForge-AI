import logging
from typing import Dict, Any, List
from app.modules.execution.execution_router import ExecutionRouter

logger = logging.getLogger("ExecutionMonitor")

class ExecutionMonitor:
    def __init__(self) -> None:
        self.router = ExecutionRouter()

    async def get_live_orders(self) -> List[Dict[str, Any]]:
        # Returns simulated or broker orders logs
        if self.router.use_alpaca:
            return []
        
        res = []
        for o in self.router.paper.orders:
            res.append({
                "broker_order_id": o["order_id"],
                "symbol": o["ticker"],
                "qty": o["quantity"],
                "side": o["side"],
                "status": o["status"],
                "timestamp": o["timestamp"]
            })
        return res

    async def get_live_positions(self) -> List[Dict[str, Any]]:
        positions = await self.router.get_positions()
        res = []
        for pos in positions:
            res.append({
                "symbol": pos.ticker,
                "qty": pos.quantity,
                "entry_price": pos.entry_price,
                "current_price": pos.market_price,
                "unrealized_pnl": pos.unrealized_pnl,
                "timestamp": pos.timestamp if hasattr(pos, "timestamp") else None
            })
        return res
