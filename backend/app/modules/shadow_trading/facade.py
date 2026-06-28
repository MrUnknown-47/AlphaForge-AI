from typing import Dict, Any, List
from app.modules.shadow_trading.service import ShadowTradingService

class ShadowTradingFacade:
    def __init__(self) -> None:
        self.service = ShadowTradingService()

    async def execute_reconciliation(self) -> Dict[str, Any]:
        return await self.service.run_reconciliation_cycle()

    def get_account(self) -> Dict[str, Any]:
        return self.service.get_account_summary()

    def get_positions(self) -> List[Dict[str, Any]]:
        return self.service.get_positions()

    def get_performance(self) -> Dict[str, Any]:
        return self.service.get_performance_stats()

    def get_execution(self) -> Dict[str, Any]:
        return self.service.get_execution_metrics()
