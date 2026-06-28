from app.shared.events import Event

class FeatureSetCommittedEvent(Event):
    """Fired when new feature vectors are persisted."""
    def __init__(self, ticker: str, timestamp: str) -> None:
        self.ticker = ticker
        self.timestamp = timestamp

    @property
    def event_name(self) -> str:
        return "feature_store.set_committed"