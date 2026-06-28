from typing import Dict, Any, List
from app.modules.operations.service import OperationsService

class OperationsFacade:
    def __init__(self) -> None:
        self.service = OperationsService()

    def get_health(self) -> Dict[str, Any]:
        return self.service.get_health_status()

    def get_models(self) -> Dict[str, Any]:
        return self.service.get_model_metrics()

    def get_portfolio(self) -> Dict[str, Any]:
        return self.service.get_portfolio_state()

    def get_incidents(self) -> List[Dict[str, Any]]:
        return self.service.get_incidents()

    def get_alerts(self) -> List[Dict[str, Any]]:
        return self.service.get_alerts()

    def get_audit(self) -> List[str]:
        return self.service.get_audit_trail()

    def get_scorecard(self) -> Dict[str, Any]:
        return self.service.get_scorecard()
