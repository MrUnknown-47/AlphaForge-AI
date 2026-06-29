import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class ExecutionOrderModel(Base):
    __tablename__ = "orders"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    broker_order_id: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    qty: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    side: Mapped[str] = mapped_column(String(16), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ExecutionFillModel(Base):
    __tablename__ = "fills"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    broker_order_id: Mapped[str] = mapped_column(String(100), nullable=False)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    qty: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ExecutionPositionModel(Base):
    __tablename__ = "positions"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False, unique=True)
    qty: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    entry_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    current_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    unrealized_pnl: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ExecutionTelemetryModel(Base):
    __tablename__ = "telemetry"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    side: Mapped[str] = mapped_column(String(16), nullable=False)
    quantity: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    requested_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    executed_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    slippage: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    commission: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)
    latency: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False) # ms
    broker_order_id: Mapped[str] = mapped_column(String(100), nullable=False)
    strategy_id: Mapped[str] = mapped_column(String(100), nullable=True)

class ExecutionPnlModel(Base):
    __tablename__ = "pnl"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    realized_pnl: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    unrealized_pnl: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    daily_pnl: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    portfolio_pnl: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    running_equity: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)

class ExecutionSlippageModel(Base):
    __tablename__ = "slippage"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    arrival_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    fill_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    slippage_bps: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class ExecutionEventModel(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    event_type: Mapped[str] = mapped_column(String(50), nullable=False) # e.g. ORDER_SUBMITTED, KILL_SWITCH
    message: Mapped[str] = mapped_column(String(255), nullable=False)

class ExecutionSessionModel(Base):
    __tablename__ = "sessions"
    __table_args__ = {"schema": "execution"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
