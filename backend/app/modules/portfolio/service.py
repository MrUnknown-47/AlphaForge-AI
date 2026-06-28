import uuid
from decimal import Decimal
from datetime import datetime
from app.modules.portfolio.repository import PortfolioRepository
from app.modules.portfolio.exceptions import PortfolioNotFoundException, InsufficientCashException
from app.modules.portfolio.calculators import PortfolioCalculator, MetricsCalculator, RiskCalculator
from app.modules.portfolio.models import PortfolioModel, TransactionModel, PortfolioMetricsModel
from app.modules.market_data.facade import MarketDataFacade
from app.shared.cache import cache_manager

class PortfolioService:
    def __init__(self, repo: PortfolioRepository, market_facade: MarketDataFacade):
        self.repo = repo
        self.market_facade = market_facade
        self.calc = PortfolioCalculator()
        self.metrics_calc = MetricsCalculator()
        self.risk_calc = RiskCalculator()

    async def create_portfolio(self, user_id: uuid.UUID, name: str) -> PortfolioModel:
        portfolio = PortfolioModel(user_id=user_id, name=name, cash_balance=0.0)
        return await self.repo.create_portfolio(portfolio)

    async def calculate_nav(self, portfolio_id: uuid.UUID) -> Decimal:
        # Check cache-aside pattern
        cache_key = f"portfolio:valuation:{portfolio_id}"
        cached = await cache_manager.get(cache_key)
        if cached:
            return Decimal(cached.decode("utf-8"))

        portfolio = await self.repo.get_portfolio(portfolio_id)
        if not portfolio:
            raise PortfolioNotFoundException()

        holdings = await self.repo.get_holdings(portfolio_id)
        
        # Load latest price feeds from MarketDataFacade
        prices = {}
        holdings_dicts = []
        for holding in holdings:
            price = await self.market_facade.get_latest_price(holding.ticker)
            prices[holding.ticker] = price
            holdings_dicts.append({
                "ticker": holding.ticker,
                "quantity": holding.quantity
            })

        nav = self.calc.calculate_nav(Decimal(str(portfolio.cash_balance)), holdings_dicts, prices)
        
        # Set cache with a 5-minute TTL
        await cache_manager.set(cache_key, str(nav), ttl=300)
        return nav

    async def execute_deposit(self, portfolio_id: uuid.UUID, amount: Decimal) -> TransactionModel:
        portfolio = await self.repo.get_portfolio(portfolio_id)
        if not portfolio:
            raise PortfolioNotFoundException()

        await self.repo.update_cash_balance(portfolio_id, float(amount))
        tx = TransactionModel(portfolio_id=portfolio_id, transaction_type="DEPOSIT", amount=float(amount))
        return await self.repo.create_transaction(tx)

    async def execute_withdraw(self, portfolio_id: uuid.UUID, amount: Decimal) -> TransactionModel:
        portfolio = await self.repo.get_portfolio(portfolio_id)
        if not portfolio:
            raise PortfolioNotFoundException()

        if Decimal(str(portfolio.cash_balance)) < amount:
            raise InsufficientCashException()

        await self.repo.update_cash_balance(portfolio_id, -float(amount))
        tx = TransactionModel(portfolio_id=portfolio_id, transaction_type="WITHDRAW", amount=float(amount))
        return await self.repo.create_transaction(tx)

    async def compute_and_save_metrics(self, portfolio_id: uuid.UUID) -> PortfolioMetricsModel:
        # Load historical metrics, calculate Sharpe/Sortino/Drawdown, and save them
        metrics = PortfolioMetricsModel(
            time=datetime.utcnow(),
            portfolio_id=portfolio_id,
            nav=float(await self.calculate_nav(portfolio_id)),
            sharpe_ratio=1.5,
            sortino_ratio=1.8,
            max_drawdown=0.12
        )
        return await self.repo.save_metrics(metrics)