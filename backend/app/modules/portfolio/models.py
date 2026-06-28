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