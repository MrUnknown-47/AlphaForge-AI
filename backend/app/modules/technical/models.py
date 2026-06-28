import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.shared.database import Base

class IndicatorsCacheModel(Base):
    __tablename__ = "indicators_cache"
    __table_args__ = {"schema": "technical"}

    time: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    rsi_14: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    macd_12_26: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    macd_signal_9: Mapped[float] = mapped_column(Numeric(10, 4), nullable=True)
    bollinger_upper: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)
    bollinger_lower: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)
    vwap: Mapped[float] = mapped_column(Numeric(20, 8), nullable=True)