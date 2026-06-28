class ResearchRepository:
    """Data access layer mapping to Research schemas."""
    def __init__(self, db_session):
        self.db = db_session\n