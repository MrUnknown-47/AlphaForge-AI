class AlertsRepository:
    """Data access layer mapping to Alerts schemas."""
    def __init__(self, db_session):
        self.db = db_session\n