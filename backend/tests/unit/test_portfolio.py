import pytest
import uuid
from decimal import Decimal
from unittest.mock import AsyncMock, MagicMock
from app.modules.portfolio.service import PortfolioService
from app.modules.portfolio.exceptions import InsufficientCashException

@pytest.mark.asyncio
async def test_portfolio_withdrawal_insufficient_funds():
    repo_mock = MagicMock()
    repo_mock.get_portfolio = AsyncMock(return_value=MagicMock(cash_balance=100.00))
    market_facade_mock = MagicMock()

    service = PortfolioService(repo_mock, market_facade_mock)
    
    with pytest.raises(InsufficientCashException):
        await service.execute_withdraw(uuid.uuid4(), Decimal("500.00"))