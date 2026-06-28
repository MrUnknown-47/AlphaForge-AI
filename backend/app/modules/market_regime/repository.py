class MarketRegimeRepository:
    """Data access layer mapping to MarketRegime schemas."""
    def __init__(self, db_session):
        self.db = db_session\n