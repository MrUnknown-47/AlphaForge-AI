import queue
from typing import Dict, Any, List

class Event:
    pass

class MarketEvent(Event):
    def __init__(self, timestamp: str, ticker: str, open_p: float, high: float, low: float, close: float, volume: float) -> None:
        self.type = 'MARKET'
        self.timestamp = timestamp
        self.ticker = ticker
        self.open = open_p
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

class SignalEvent(Event):
    def __init__(self, ticker: str, timestamp: str, action: str, confidence: float) -> None:
        self.type = 'SIGNAL'
        self.ticker = ticker
        self.timestamp = timestamp
        self.action = action # BUY, SELL, HOLD
        self.confidence = confidence

class OrderEvent(Event):
    def __init__(self, ticker: str, qty: float, side: str, order_type: str = 'MARKET') -> None:
        self.type = 'ORDER'
        self.ticker = ticker
        self.qty = qty
        self.side = side
        self.order_type = order_type

class FillEvent(Event):
    def __init__(self, ticker: str, timestamp: str, qty: float, side: str, fill_price: float, commission: float = 0.0) -> None:
        self.type = 'FILL'
        self.ticker = ticker
        self.timestamp = timestamp
        self.qty = qty
        self.side = side
        self.fill_price = fill_price
        self.commission = commission

class EventDrivenBacktestEngine:
    def __init__(self) -> None:
        self.event_queue = queue.Queue()
        self.trades = []
        self.equity_curve = []
        self.cash = 100000.0
        self.positions = {}

    def run(self) -> None:
        while not self.event_queue.empty():
            event = self.event_queue.get()
            if event.type == 'MARKET':
                pass
            elif event.type == 'SIGNAL':
                # Map signal to order
                order = OrderEvent(event.ticker, 10.0, event.action)
                self.event_queue.put(order)
            elif event.type == 'ORDER':
                # Simulates instant fill
                fill = FillEvent(event.ticker, "2026-06-28T16:00:00", event.qty, event.side, fill_price=150.0)
                self.event_queue.put(fill)
            elif event.type == 'FILL':
                self.trades.append({
                    "symbol": event.ticker,
                    "price": event.fill_price,
                    "qty": event.qty,
                    "side": event.side,
                    "timestamp": event.timestamp
                })
