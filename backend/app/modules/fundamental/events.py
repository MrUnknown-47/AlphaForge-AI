from app.shared.events import Event

class FundamentalsSyncedEvent(Event):
    """Fired in-memory when new statement points are committed."""
    def __init__(self, ticker: str, fiscal_year: int, fiscal_period: str) -> None:
        self.ticker = ticker
        self.fiscal_year = fiscal_year
        self.fiscal_period = fiscal_period

    @property
    def event_name(self) -> str:
        return "fundamental.synced"