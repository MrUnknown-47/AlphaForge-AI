import uuid
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, ForeignKey, TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.shared.database import Base

class NewsArticleModel(Base):
    __tablename__ = "news_articles"
    __table_args__ = {"schema": "sentiment"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    headline: Mapped[str] = mapped_column(String(512), nullable=False)
    content: Mapped[str] = mapped_column(TEXT, nullable=True)
    url: Mapped[str] = mapped_column(String(1024), nullable=True, unique=True, index=True)
    published_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    sentiment_scores: Mapped[list["SentimentScoreModel"]] = relationship(back_populates="article", cascade="all, delete-orphan")

class SentimentScoreModel(Base):
    __tablename__ = "sentiment_scores"
    __table_args__ = {"schema": "sentiment"}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    article_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sentiment.news_articles.id", ondelete="CASCADE"), nullable=False)
    ticker: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    sentiment_label: Mapped[str] = mapped_column(String(16), nullable=False) # BULLISH, BEARISH, NEUTRAL
    confidence_score: Mapped[float] = mapped_column(Numeric(5, 4), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    article: Mapped["NewsArticleModel"] = relationship(back_populates="sentiment_scores")