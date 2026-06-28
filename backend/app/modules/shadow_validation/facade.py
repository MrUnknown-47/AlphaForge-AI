from typing import Dict, Any, List
from app.modules.shadow_validation.service import ShadowValidationService

class ShadowValidationFacade:
    def __init__(self) -> None:
        self.service = ShadowValidationService()

    async def execute_cycle(self) -> Dict[str, Any]:
        return await self.service.run_validation_cycle()

    def get_daily_logs(self) -> List[Dict[str, Any]]:
        return self.service.get_daily()

    def get_weekly_logs(self) -> List[Dict[str, Any]]:
        return self.service.get_weekly()

    def get_monthly_logs(self) -> List[Dict[str, Any]]:
        return self.service.get_monthly()

    def get_execution_stats(self) -> Dict[str, Any]:
        return self.service.get_execution()

    def get_capacity_stats(self) -> List[Dict[str, Any]]:
        return self.service.get_capacity()

    def get_scorecard_details(self) -> Dict[str, Any]:
        return self.service.get_scorecard()
