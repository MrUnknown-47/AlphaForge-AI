import logging
from decimal import Decimal
from typing import Any
from app.modules.sentiment.repository import SentimentRepository
from app.modules.sentiment.news_provider import GoogleNewsRSSProvider, YahooFinanceNewsProvider, RedditApiProvider
from app.modules.sentiment.sentiment_engine import sentiment_engine
from app.modules.sentiment.models import NewsArticleModel
from app.shared.cache import cache_manager

logger = logging.getLogger(__name__)

class SentimentService:
    def __init__(self, repo: SentimentRepository) -> None:
        self.repo = repo
        self.providers = [
            GoogleNewsRSSProvider(),
            YahooFinanceNewsProvider(),
            RedditApiProvider()
        ]

    async def get_latest_sentiment_for_ticker(self, ticker: str, limit: int = 20) -> list[NewsArticleModel]:
        return await self.repo.get_news_with_scores(ticker, limit)

    async def scrape_and_analyze_ticker(self, ticker: str, limit: int = 5) -> None:
        logger.info(f"Initiating sentiment scraping loop for ticker: {ticker}...")
        
        # 1. Fetch news from RSS & APIs concurrently
        all_raw_articles = []
        import asyncio
        tasks = [provider.fetch_ticker_news(ticker, limit) for provider in self.providers]
        results = await asyncio.gather(*tasks)
        for res in results:
            all_raw_articles.extend(res)

        # 2. Check duplicates in DB (deduplication check via URLs)
        uniques = []
        for art in all_raw_articles:
            existing = await self.repo.get_article_by_url(art["url"])
            if not existing:
                uniques.append(art)

        if not uniques:
            logger.info(f"No new unique articles found for {ticker}.")
            return

        logger.info(f"Found {len(uniques)} new unique articles for {ticker}. Running sentiment inference...")

        # 3. Batch sentiment analysis using FinBERT pipeline
        headlines = [a["headline"] for a in uniques]
        inference_results = sentiment_engine.analyze_batch(headlines)

        # 4. Save new articles and map executions
        scores_to_insert = []
        
        for art, inf in zip(uniques, inference_results):
            # Save the article model first to get UUID
            article_model = NewsArticleModel(
                source=art["source"],
                headline=art["headline"],
                content=art["content"],
                url=art["url"],
                published_at=art["published_at"]
            )
            saved_article = await self.repo.save_article(article_model)
            
            scores_to_insert.append({
                "article_id": saved_article.id,
                "ticker": ticker,
                "sentiment_label": inf["label"],
                "confidence_score": Decimal(str(inf["score"]))
            })

        # Batch insert scores
        await self.repo.insert_sentiment_scores_batch(scores_to_insert)

        # 5. Calculate average aggregate score and update Redis
        # Numeric values: BULLISH = 1, BEARISH = -1, NEUTRAL = 0
        total_val = 0.0
        for s in scores_to_insert:
            val = 1.0 if s["sentiment_label"] == "BULLISH" else -1.0 if s["sentiment_label"] == "BEARISH" else 0.0
            # Weight by confidence score
            total_val += val * float(s["confidence_score"])
        
        mean_score = total_val / len(scores_to_insert) if scores_to_insert else 0.0

        cache_key = f"sentiment:latest:{ticker}"
        cache_payload = {
            "ticker": ticker,
            "mean_sentiment": mean_score,
            "sample_size": len(scores_to_insert),
            "last_updated": datetime.utcnow().isoformat()
        }
        await cache_manager.set_json(cache_key, cache_payload, ttl=86400) # Cache for 24 hours
        logger.info(f"Successfully sync-completed sentiment evaluation for {ticker}. Mean: {mean_score:.2f}")

# Import datetime inside service to prevent name conflicts
from datetime import datetime