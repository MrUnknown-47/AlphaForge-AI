class HedgefundRepository:
    """Data access layer mapping to Hedgefund schemas."""
    def __init__(self, db_session):
        self.db = db_session\n