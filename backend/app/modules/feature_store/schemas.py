import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from decimal import Decimal

class FeatureQuery(BaseModel):
    tickers: list[str]
    start_date: datetime
    end_date: datetime

class TechnicalFeaturesResponse(BaseModel):
    time: datetime
    ticker: str
    rsi: Decimal | None
    macd_line: Decimal | None
    macd_signal: Decimal | None
    adx: Decimal | None
    atr: Decimal | None
    bollinger_upper: Decimal | None
    bollinger_lower: Decimal | None
    vwap: Decimal | None

    class Config:
        from_attributes = True

class MarketFeaturesResponse(BaseModel):
    time: datetime
    ticker: str
    returns_1d: Decimal | None
    returns_5d: Decimal | None
    volatility_20: Decimal | None
    zscore_20: Decimal | None
    rolling_std_20: Decimal | None
    rolling_mean_20: Decimal | None

    class Config:
        from_attributes = True

class FundamentalFeaturesResponse(BaseModel):
    time: datetime
    ticker: str
    pe_ratio: Decimal | None
    pb_ratio: Decimal | None
    roe: Decimal | None
    roa: Decimal | None
    debt_to_equity: Decimal | None

    class Config:
        from_attributes = True

class SentimentFeaturesResponse(BaseModel):
    time: datetime
    ticker: str
    sentiment_mean: Decimal | None
    sentiment_count: int | None
    sentiment_change: Decimal | None

    class Config:
        from_attributes = True

class FeatureSetResponse(BaseModel):
    ticker: str
    timestamp: datetime
    technical: TechnicalFeaturesResponse | None = None
    market: MarketFeaturesResponse | None = None
    fundamental: FundamentalFeaturesResponse | None = None
    sentiment: SentimentFeaturesResponse | None = None

class BackfillRequest(BaseModel):
    tickers: list[str]
    start_date: datetime
    end_date: datetime