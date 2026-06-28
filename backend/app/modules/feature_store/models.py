import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class TechnicalFeaturesModel(Base):
    __tablename__ = "technical_features"
    __table_args__ = {"schema": "feature_store"}

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    
    rsi: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    macd: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    atr: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)
    bollinger_width: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)
    ema_10: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)
    ema_200: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)

class MarketFeaturesModel(Base):
    __tablename__ = "market_features"
    __table_args__ = {"schema": "feature_store"}

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    
    returns_1d: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    returns_5d: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    returns_20d: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    realized_vol_20: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    market_beta: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    spy_correlation: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)
    qqq_correlation: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)

class FundamentalFeaturesModel(Base):
    __tablename__ = "fundamental_features"
    __table_args__ = {"schema": "feature_store"}

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    
    pe_ratio: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    pb_ratio: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    roe: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    debt_to_equity: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)

class SentimentFeaturesModel(Base):
    __tablename__ = "sentiment_features"
    __table_args__ = {"schema": "feature_store"}

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    
    sentiment_mean: Mapped[float] = mapped_column(Numeric(5, 4), nullable=True)
    sentiment_change: Mapped[float] = mapped_column(Numeric(10, 6), nullable=True)