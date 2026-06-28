from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.fundamental.repository import FundamentalRepository
from app.modules.fundamental.service import FundamentalService
from app.modules.fundamental.facade import FundamentalFacade

async def get_fundamental_repo(db: AsyncSession = Depends(get_db)) -> FundamentalRepository:
    return FundamentalRepository(db)

async def get_fundamental_service(
    repo: FundamentalRepository = Depends(get_fundamental_repo)
) -> FundamentalService:
    return FundamentalService(repo)

async def get_fundamental_facade(
    service: FundamentalService = Depends(get_fundamental_service)
) -> FundamentalFacade:
    return FundamentalFacade(service)
