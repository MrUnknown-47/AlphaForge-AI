class OptimizationRepository:
    """Data access layer mapping to Optimization schemas."""
    def __init__(self, db_session):
        self.db = db_session\n