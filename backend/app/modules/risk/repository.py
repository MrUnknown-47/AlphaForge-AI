class RiskRepository:
    """Data access layer mapping to Risk schemas."""
    def __init__(self, db_session):
        self.db = db_session\n