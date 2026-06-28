from app.shared.events import Event

class IndicatorsRecalculatedEvent(Event):
    """Fired in-memory when new indicator points are committed to Postgres."""
    def __init__(self, ticker: str, timestamp: str) -> None:
        self.ticker = ticker
        self.timestamp = timestamp

    @property
    def event_name(self) -> str:
        return "technical.indicators_recalculated"