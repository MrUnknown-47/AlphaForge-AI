from app.modules.execution.alpaca_adapter import AlpacaAdapter
from app.modules.execution.paper_engine import PaperTradingEngine
from app.modules.execution.order_models import OrderRequest, OrderResponse, PositionResponse, AccountResponse
from app.modules.execution.risk_checks import RiskChecks
from app.config import settings
from typing import List, Dict, Any

class ExecutionRouter:
    def __init__(self) -> None:
        self.alpaca = AlpacaAdapter()
        self.paper = PaperTradingEngine()
        self.risk = RiskChecks()
        self.use_alpaca = settings.BROKER == "ALPACA"

    async def get_account(self) -> AccountResponse:
        if self.use_alpaca:
            return await self.alpaca.get_account()
        return self.paper.get_account()

    async def get_positions(self) -> List[PositionResponse]:
        if self.use_alpaca:
            return await self.alpaca.get_positions()
        return self.paper.get_positions()

    async def route_order(self, req: OrderRequest) -> OrderResponse:
        # Pre-execution risk checks
        if not self.risk.validate_order(req.ticker, req.quantity, 1.5):
            raise ValueError("Order rejected by risk checks")

        if self.use_alpaca:
            return await self.alpaca.place_order(
                req.ticker, req.side, req.quantity, req.order_type, req.price
            )
        
        # Local paper engine fill simulation
        price = req.price or 150.0
        return self.paper.execute_order(req.ticker, req.side, req.quantity, price)

    async def close_position(self, ticker: str) -> Dict[str, Any]:
        if self.use_alpaca:
            return await self.alpaca.close_position(ticker)
        return self.paper.close_position(ticker)
