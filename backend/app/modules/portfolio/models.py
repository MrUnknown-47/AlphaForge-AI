import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.shared.database import Base

class PortfolioModel(Base):
    __tablename__ = "portfolios"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(nullable=False, index=True) # Logical relation to auth.users
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    cash_balance: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    holdings: Mapped[list["HoldingModel"]] = relationship(back_populates="portfolio", cascade="all, delete-orphan")
    transactions: Mapped[list["TransactionModel"]] = relationship(back_populates="portfolio", cascade="all, delete-orphan")

class HoldingModel(Base):
    __tablename__ = "holdings"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    portfolio_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("portfolio.portfolios.id", ondelete="CASCADE"), nullable=False)
    ticker: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    quantity: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    portfolio: Mapped["PortfolioModel"] = relationship(back_populates="holdings")

class TransactionModel(Base):
    __tablename__ = "transactions"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    portfolio_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("portfolio.portfolios.id", ondelete="CASCADE"), nullable=False)
    transaction_type: Mapped[str] = mapped_column(String(16), nullable=False) # DEPOSIT, WITHDRAW, TRADE
    amount: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    portfolio: Mapped["PortfolioModel"] = relationship(back_populates="transactions")

class PortfolioMetricsModel(Base):
    __tablename__ = "portfolio_metrics"
    __table_args__ = {"schema": "portfolio"}

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    portfolio_id: Mapped[uuid.UUID] = mapped_column(primary_key=True) # Logical relation (for hypertable compatibility)
    nav: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    sharpe_ratio: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    sortino_ratio: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    max_drawdown: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)

class PortfolioAccountModel(Base):
    __tablename__ = "accounts"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    account_id: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    equity: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    cash: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    buying_power: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    portfolio_value: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    maintenance_margin: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)

class PortfolioPositionModel(Base):
    __tablename__ = "positions"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    quantity: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    avg_price: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    market_price: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    market_value: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    unrealized_pnl: Mapped[float] = mapped_column(Numeric(20, 8), default=0.0)
    unrealized_pct: Mapped[float] = mapped_column(Numeric(10, 4), default=0.0)

class PortfolioOrderModel(Base):
    __tablename__ = "orders"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    order_id: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    qty: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    side: Mapped[str] = mapped_column(String(16), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False)

class PortfolioSnapshotModel(Base):
    __tablename__ = "snapshots"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    equity: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    cash: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)

class PortfolioMetricsHistoryModel(Base):
    __tablename__ = "metrics"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    sharpe: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    sortino: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    calmar: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    max_drawdown: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    volatility: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    beta: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    alpha: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)

class PortfolioAllocationModel(Base):
    __tablename__ = "allocations"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    weight: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class PortfolioRiskMetricsModel(Base):
    __tablename__ = "risk_metrics"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    var: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    cvar: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    leverage: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
    concentration: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)