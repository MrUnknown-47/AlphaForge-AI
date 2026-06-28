from app.modules.fundamental.service import FundamentalService
from app.modules.fundamental.schemas import FinancialStatementResponse

class FundamentalFacade:
    """
    Interface gateway for feature store or optimization engines to load company metrics.
    """
    def __init__(self, service: FundamentalService):
        self._service = service

    async def get_quarterly_statements(self, ticker: str, limit: int = 20) -> list[FinancialStatementResponse]:
        models = await self._service.get_statements(ticker, limit)
        return [FinancialStatementResponse.from_orm(m) for m in models]