from app.shared.events import Event

class OrderSubmittedEvent(Event):
    """Fired when an order is validated and enters the matching engine."""
    def __init__(self, order_id: str, ticker: str, side: str, qty: float) -> None:
        self.order_id = order_id
        self.ticker = ticker
        self.side = side
        self.qty = qty

    @property
    def event_name(self) -> str:
        return "trading.order_submitted"

class OrderFilledEvent(Event):
    """Fired on partial or full fill executions to adjust holding balances."""
    def __init__(self, order_id: str, execution_id: str, price: float, qty: float) -> None:
        self.order_id = order_id
        self.execution_id = execution_id
        self.price = price
        self.qty = qty

    @property
    def event_name(self) -> str:
        return "trading.order_filled"