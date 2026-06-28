import uuid
from typing import Dict, Any, List
from app.modules.broker.interface import BrokerInterface
from app.modules.trading.paper_trading import PaperLedger, PaperExecutionEngine, RiskController
from app.config import settings

class PaperBroker(BrokerInterface):
    def __init__(self, ledger: PaperLedger = None) -> None:
        self.ledger = ledger or PaperLedger(settings.PAPER_STARTING_CAPITAL)
        self.engine = PaperExecutionEngine(self.ledger)
        self.risk = RiskController(self.ledger)
        # Mock current prices dictionary for position valuations
        self.prices = {
            "AAPL": 182.50, "MSFT": 420.10, "NVDA": 122.50, "GOOGL": 170.10,
            "AMZN": 185.20, "META": 480.30, "TSLA": 178.50, "AMD": 160.20,
            "SPY": 540.30, "QQQ": 450.40
        }

    async def get_account(self) -> Dict[str, Any]:
        val = self.ledger.get_portfolio_value(self.prices)
        return {
            "account_id": "PAPER_ACCOUNT_123",
            "cash": self.ledger.cash,
            "portfolio_value": val,
            "buying_power": self.ledger.cash
        }

    async def get_positions(self) -> List[Dict[str, Any]]:
        pos_list = []
        for ticker, pos in self.ledger.positions.items():
            qty = pos["quantity"]
            price = self.prices.get(ticker, pos["entry_price"])
            val = qty * price
            pnl = qty * (price - pos["entry_price"])
            pos_list.append({
                "ticker": ticker,
                "quantity": qty,
                "entry_price": pos["entry_price"],
                "market_value": val,
                "unrealized_pnl": pnl
            })
        return pos_list

    async def place_order(
        self, ticker: str, side: str, qty: float, type: str = "MARKET", price: float = None
    ) -> Dict[str, Any]:
        trade_price = price or self.prices.get(ticker, 100.0)
        
        # Enforce pre-trade risk controls
        if not self.risk.verify_pre_trade_limits(ticker, qty, trade_price, self.prices):
            return {
                "order_id": str(uuid.uuid4()),
                "ticker": ticker,
                "side": side,
                "type": type,
                "quantity": qty,
                "price": trade_price,
                "status": "REJECTED"
            }

        # Side: convert to LONG/SHORT for our execution engine
        direction = "LONG" if side == "BUY" else "SHORT"
        success = self.engine.execute_order(ticker, direction, qty, trade_price)
        
        status_str = "FILLED" if success else "REJECTED"
        return {
            "order_id": str(uuid.uuid4()),
            "ticker": ticker,
            "side": side,
            "type": type,
            "quantity": qty,
            "price": trade_price,
            "status": status_str
        }

    async def close_position(self, ticker: str) -> Dict[str, Any]:
        if ticker not in self.ledger.positions:
            return {"status": "NO_POSITION"}
            
        pos = self.ledger.positions[ticker]
        qty = abs(pos["quantity"])
        side = "SELL" if pos["quantity"] > 0 else "BUY"
        return await self.place_order(ticker, side, qty)
