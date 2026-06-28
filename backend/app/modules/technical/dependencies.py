from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.technical.repository import TechnicalRepository
from app.modules.technical.service import TechnicalService
from app.modules.technical.facade import TechnicalFacade
from app.modules.market_data.facade import MarketDataFacade
from app.modules.market_data.dependencies import get_market_facade

async def get_technical_repo(db: AsyncSession = Depends(get_db)) -> TechnicalRepository:
    return TechnicalRepository(db)

async def get_technical_service(
    repo: TechnicalRepository = Depends(get_technical_repo),
    market_facade: MarketDataFacade = Depends(get_market_facade)
) -> TechnicalService:
    return TechnicalService(repo, market_facade)

async def get_technical_facade(
    service: TechnicalService = Depends(get_technical_service)
) -> TechnicalFacade:
    return TechnicalFacade(service)
