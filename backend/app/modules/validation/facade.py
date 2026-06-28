from typing import Dict, Any
from app.modules.validation.service import ValidationService

class ValidationFacade:
    def __init__(self) -> None:
        self.service = ValidationService()

    async def execute_cycle(self) -> Dict[str, Any]:
        return await self.service.run_validation_cycle()

    def get_performance(self) -> Dict[str, Any]:
        return self.service.get_performance_stats()

    def get_risk(self) -> Dict[str, Any]:
        return self.service.get_risk_stats()

    def get_drift(self) -> Dict[str, Any]:
        return self.service.get_drift_stats()

    def get_scorecard(self) -> Dict[str, Any]:
        return self.service.get_scorecard()
