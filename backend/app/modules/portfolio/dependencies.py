from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.portfolio.repository import PortfolioRepository
from app.modules.portfolio.service import PortfolioService
from app.modules.portfolio.facade import PortfolioFacade
from app.modules.market_data.facade import MarketDataFacade
from app.modules.market_data.dependencies import get_market_facade

async def get_portfolio_repo(db: AsyncSession = Depends(get_db)) -> PortfolioRepository:
    return PortfolioRepository(db)

async def get_portfolio_service(
    repo: PortfolioRepository = Depends(get_portfolio_repo),
    market_facade: MarketDataFacade = Depends(get_market_facade)
) -> PortfolioService:
    return PortfolioService(repo, market_facade)

async def get_portfolio_facade(
    service: PortfolioService = Depends(get_portfolio_service)
) -> PortfolioFacade:
    return PortfolioFacade(service)
