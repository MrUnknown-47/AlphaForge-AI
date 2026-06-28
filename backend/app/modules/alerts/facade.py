class AlertsFacade:
    """
    Public interface for the Alerts module.
    Only methods defined in this Facade should be imported or invoked by other modules.
    """
    def __init__(self, service):
        self._service = service\n