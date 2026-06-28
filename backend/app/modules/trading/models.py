import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.shared.database import Base

class OrderModel(Base):
    __tablename__ = "orders"
    __table_args__ = {"schema": "trading"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    portfolio_id: Mapped[uuid.UUID] = mapped_column(nullable=False, index=True) # Logical ref
    ticker: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    side: Mapped[str] = mapped_column(String(8), nullable=False) # BUY, SELL
    type: Mapped[str] = mapped_column(String(16), nullable=False) # MARKET, LIMIT, STOP, STOP_LIMIT
    quantity: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="PENDING") # PENDING, PARTIAL_FILL, FILLED, CANCELLED, REJECTED
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    executions: Mapped[list["ExecutionModel"]] = relationship(back_populates="order", cascade="all, delete-orphan")
    order_events: Mapped[list["OrderEventModel"]] = relationship(back_populates="order", cascade="all, delete-orphan")

class ExecutionModel(Base):
    __tablename__ = "executions"
    __table_args__ = {"schema": "trading"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("trading.orders.id", ondelete="CASCADE"), nullable=False)
    execution_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    executed_quantity: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    fee: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    executed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    order: Mapped["OrderModel"] = relationship(back_populates="executions")

class PositionModel(Base):
    __tablename__ = "positions"
    __table_args__ = {"schema": "trading"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    portfolio_id: Mapped[uuid.UUID] = mapped_column(nullable=False, index=True) # Logical ref
    ticker: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    quantity: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    average_entry_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    last_updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

class OrderEventModel(Base):
    __tablename__ = "order_events"
    __table_args__ = {"schema": "trading"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("trading.orders.id", ondelete="CASCADE"), nullable=False)
    event_type: Mapped[str] = mapped_column(String(64), nullable=False) # SUBMITTED, REJECTED, FILLED
    payload: Mapped[dict] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    order: Mapped["OrderModel"] = relationship(back_populates="order_events")