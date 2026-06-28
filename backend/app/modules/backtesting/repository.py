class BacktestingRepository:
    """Data access layer mapping to Backtesting schemas."""
    def __init__(self, db_session):
        self.db = db_session\n