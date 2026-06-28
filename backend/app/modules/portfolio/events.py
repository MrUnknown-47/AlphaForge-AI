from app.shared.events import Event

class PortfolioCreatedEvent(Event):
    """Triggered on database commitment of a new portfolio entity."""
    def __init__(self, portfolio_id: str, user_id: str) -> None:
        self.portfolio_id = portfolio_id
        self.user_id = user_id

    @property
    def event_name(self) -> str:
        return "portfolio.created"

class TransactionRecordedEvent(Event):
    """Fired when deposits, withdrawals, or trades alter cash levels."""
    def __init__(self, portfolio_id: str, tx_type: str, amount: float) -> None:
        self.portfolio_id = portfolio_id
        self.tx_type = tx_type
        self.amount = amount

    @property
    def event_name(self) -> str:
        return "portfolio.transaction_recorded"