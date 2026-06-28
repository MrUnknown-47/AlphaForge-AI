class OptimizationFacade:
    """
    Public interface for the Optimization module.
    Only methods defined in this Facade should be imported or invoked by other modules.
    """
    def __init__(self, service):
        self._service = service\n