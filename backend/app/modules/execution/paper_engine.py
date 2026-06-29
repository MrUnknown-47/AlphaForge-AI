from typing import Dict, Any, List
from datetime import datetime
from app.modules.execution.order_models import OrderResponse, PositionResponse, AccountResponse
import uuid

class PaperTradingEngine:
    def __init__(self) -> None:
        self.cash = 100000.0
        self.positions: Dict[str, Dict[str, Any]] = {}
        self.orders: List[Dict[str, Any]] = []

    def get_account(self) -> AccountResponse:
        equity = self.cash
        for pos in self.positions.values():
            equity += pos["qty"] * pos["current_price"]
        return AccountResponse(
            account_id="PAPER_ENGINE_MOCK",
            status="ACTIVE",
            cash=self.cash,
            buying_power=self.cash * 4.0,
            equity=equity,
            multiplier=4.0
        )

    def get_positions(self) -> List[PositionResponse]:
        res = []
        for ticker, pos in self.positions.items():
            current_val = pos["qty"] * pos["current_price"]
            entry_val = pos["qty"] * pos["avg_entry_price"]
            res.append(PositionResponse(
                ticker=ticker,
                quantity=pos["qty"],
                entry_price=pos["avg_entry_price"],
                market_value=current_val,
                unrealized_pnl=current_val - entry_val
            ))
        return res

    def execute_order(self, ticker: str, side: str, qty: float, price: float) -> OrderResponse:
        order_id = f"paper_ord_{uuid.uuid4().hex[:8]}"
        fill_price = price
        
        # Adjust ledger balances
        cost = fill_price * qty
        if side.upper() == "BUY":
            self.cash -= cost
            if ticker in self.positions:
                old_qty = self.positions[ticker]["qty"]
                old_avg = self.positions[ticker]["avg_entry_price"]
                new_qty = old_qty + qty
                new_avg = ((old_avg * old_qty) + cost) / new_qty
                self.positions[ticker]["qty"] = new_qty
                self.positions[ticker]["avg_entry_price"] = new_avg
                self.positions[ticker]["current_price"] = fill_price
            else:
                self.positions[ticker] = {
                    "qty": qty,
                    "avg_entry_price": fill_price,
                    "current_price": fill_price
                }
        else: # SELL
            self.cash += cost
            if ticker in self.positions:
                old_qty = self.positions[ticker]["qty"]
                new_qty = old_qty - qty
                if new_qty <= 0:
                    del self.positions[ticker]
                else:
                    self.positions[ticker]["qty"] = new_qty
                    self.positions[ticker]["current_price"] = fill_price

        order = {
            "order_id": order_id,
            "ticker": ticker,
            "side": side,
            "quantity": qty,
            "price": fill_price,
            "status": "FILLED",
            "timestamp": datetime.utcnow()
        }
        self.orders.append(order)
        return OrderResponse(**order)

    def close_position(self, ticker: str) -> Dict[str, Any]:
        if ticker in self.positions:
            pos = self.positions[ticker]
            self.execute_order(ticker, "SELL", pos["qty"], pos["current_price"])
        return {"status": "CLOSED", "ticker": ticker, "order_id": "PAPER_CLOSE"}
