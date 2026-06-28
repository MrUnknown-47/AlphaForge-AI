# Background Celery task stubs for the Technical module operations

def recalculate_indicators_job() -> None:
    """
    Scheduled worker job that retrieves historical price data for active tickers,
    resolves calculations (SMA, RSI, Bollinger Bands), and upserts them to
    technical.indicators_cache.
    """
    pass

def prune_indicators_cache_weekly() -> None:
    """
    Cleans up old indicator caches from the database to manage TimescaleDB
    table index size constraints.
    """
    pass