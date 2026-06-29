import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, Boolean, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class BacktestStrategyModel(Base):
    __tablename__ = "strategies"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    parameters: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class BacktestRunModel(Base):
    __tablename__ = "runs"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    strategy_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="PENDING")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    completed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

class BacktestOrderModel(Base):
    __tablename__ = "orders"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    qty: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    side: Mapped[str] = mapped_column(String(16), nullable=False)
    order_type: Mapped[str] = mapped_column(String(32), default="MARKET")
    status: Mapped[str] = mapped_column(String(32), default="FILLED")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class BacktestTradeModel(Base):
    __tablename__ = "trades"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    qty: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class BacktestPositionModel(Base):
    __tablename__ = "positions"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    symbol: Mapped[str] = mapped_column(String(16), nullable=False)
    qty: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    avg_price: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

class BacktestSnapshotModel(Base):
    __tablename__ = "snapshots"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    equity: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)
    cash: Mapped[float] = mapped_column(Numeric(20, 8), nullable=False)

class BacktestMetricsModel(Base):
    __tablename__ = "metrics"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False, unique=True)
    sharpe: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    sortino: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    calmar: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    max_drawdown: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    win_rate: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    profit_factor: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)

class BacktestOptimizationModel(Base):
    __tablename__ = "optimizations"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    strategy_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    best_parameters: Mapped[dict] = mapped_column(JSON, default=dict)
    metric_name: Mapped[str] = mapped_column(String(50), nullable=False)
    metric_value: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)

class BacktestWalkforwardModel(Base):
    __tablename__ = "walkforward"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    strategy_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    train_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    train_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    val_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    val_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

class BacktestMontecarloModel(Base):
    __tablename__ = "montecarlo"
    __table_args__ = {"schema": "backtest"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    simulation_paths: Mapped[int] = mapped_column(Integer, default=1000)
    ruin_probability: Mapped[float] = mapped_column(Numeric(10, 4), nullable=False)
