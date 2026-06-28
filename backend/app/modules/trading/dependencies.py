from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.database import get_db
from app.modules.trading.repository import TradingRepository
from app.modules.trading.service import TradingService
from app.modules.trading.facade import TradingFacade
from app.modules.trading.order_validator import OrderValidator
from app.modules.trading.risk_engine import RiskEngine
from app.modules.trading.execution_engine import ExecutionEngine
from app.modules.trading.matching_engine import MatchingEngine
from app.modules.trading.ledger import LedgerEngine
from app.modules.portfolio.facade import PortfolioFacade
from app.modules.portfolio.dependencies import get_portfolio_facade
from app.modules.market_data.facade import MarketDataFacade
from app.modules.market_data.dependencies import get_market_facade

async def get_trading_repo(db: AsyncSession = Depends(get_db)) -> TradingRepository:
    return TradingRepository(db)

async def get_trading_service(
    repo: TradingRepository = Depends(get_trading_repo),
    portfolio_facade: PortfolioFacade = Depends(get_portfolio_facade),
    market_facade: MarketDataFacade = Depends(get_market_facade)
) -> TradingService:
    validator = OrderValidator()
    risk_engine = RiskEngine(portfolio_facade)
    matching_engine = MatchingEngine()
    ledger_engine = LedgerEngine(portfolio_facade)
    exec_engine = ExecutionEngine(matching_engine, ledger_engine)
    
    return TradingService(repo, market_facade, validator, risk_engine, exec_engine)

async def get_trading_facade(
    service: TradingService = Depends(get_trading_service)
) -> TradingFacade:
    return TradingFacade(service)
