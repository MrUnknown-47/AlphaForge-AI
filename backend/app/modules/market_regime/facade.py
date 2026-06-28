class MarketRegimeFacade:
    """
    Public interface for the MarketRegime module.
    Only methods defined in this Facade should be imported or invoked by other modules.
    """
    def __init__(self, service):
        self._service = service\n