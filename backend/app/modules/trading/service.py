import uuid
from decimal import Decimal
from datetime import datetime
from app.modules.trading.repository import TradingRepository
from app.modules.trading.order_validator import OrderValidator
from app.modules.trading.risk_engine import RiskEngine
from app.modules.trading.execution_engine import ExecutionEngine
from app.modules.trading.models import OrderModel, OrderEventModel
from app.modules.trading.exceptions import OrderNotFoundException, InvalidOrderStatusException
from app.modules.trading.schemas import OrderCreate
from app.modules.market_data.facade import MarketDataFacade

class TradingService:
    def __init__(
        self,
        repo: TradingRepository,
        market_facade: MarketDataFacade,
        validator: OrderValidator,
        risk_engine: RiskEngine,
        exec_engine: ExecutionEngine
    ):
        self.repo = repo
        self.market_facade = market_facade
        self.validator = validator
        self.risk_engine = risk_engine
        self.exec_engine = exec_engine

    async def submit_order(self, data: OrderCreate) -> OrderModel:
        # 1. Fetch current price from MarketDataFacade
        current_price = await self.market_facade.get_latest_price(data.ticker)

        # 2. Map data to OrderModel
        order = OrderModel(
            portfolio_id=data.portfolio_id,
            ticker=data.ticker,
            side=data.side,
            type=data.type,
            quantity=float(data.quantity),
            price=float(data.price) if data.price else None,
            status="PENDING"
        )

        # 3. Perform input parameters checks
        self.validator.validate_order(order, current_price)

        # 4. Perform risk limits check (cash availability, margin exposures)
        await self.risk_engine.verify_pre_trade_limits(order, current_price)

        # 5. Persist order entity
        saved_order = await self.repo.save_order(order)
        
        # Log event audit
        event = OrderEventModel(order_id=saved_order.id, event_type="SUBMITTED")
        await self.repo.save_order_event(event)

        # 6. Execute Order against the active Broker Abstraction Layer
        from app.modules.broker.service import get_broker
        broker = get_broker()
        broker_res = await broker.place_order(
            ticker=saved_order.ticker,
            side=saved_order.side,
            qty=saved_order.quantity,
            type=saved_order.type,
            price=saved_order.price
        )
        saved_order.status = broker_res.get("status", "FILLED")
        
        # Persist updated status
        return await self.repo.save_order(saved_order)

    async def cancel_order(self, order_id: uuid.UUID) -> None:
        order = await self.repo.get_order(order_id)
        if not order:
            raise OrderNotFoundException()

        if order.status not in ("PENDING", "PARTIAL_FILL"):
            raise InvalidOrderStatusException("Only pending or partially filled orders can be cancelled")

        order.status = "CANCELLED"
        await self.repo.save_order(order)

        # Log event audit
        event = OrderEventModel(order_id=order.id, event_type="CANCELLED")
        await self.repo.save_order_event(event)