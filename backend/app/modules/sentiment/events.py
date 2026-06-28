from app.shared.events import Event

class SentimentAnalyzedEvent(Event):
    """Fired in-memory when a batch of news articles is scored and saved."""
    def __init__(self, ticker: str, article_count: int, mean_sentiment: float) -> None:
        self.ticker = ticker
        self.article_count = article_count
        self.mean_sentiment = mean_sentiment

    @property
    def event_name(self) -> str:
        return "sentiment.analyzed"