import logging
import asyncio
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any
import httpx
from email.utils import parsedate_to_datetime

logger = logging.getLogger(__name__)

class NewsProvider(ABC):
    @abstractmethod
    async def fetch_ticker_news(self, ticker: str, limit: int = 10) -> list[dict[str, Any]]:
        pass


class GoogleNewsRSSProvider(NewsProvider):
    def __init__(self) -> None:
        self.client = httpx.AsyncClient(timeout=10.0)

    async def fetch_ticker_news(self, ticker: str, limit: int = 10) -> list[dict[str, Any]]:
        # Google News RSS Search query
        url = f"https://news.google.com/rss/search?q={ticker}+stock&hl=en-US&gl=US&ceid=US:en"
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            
            # Parse XML
            root = ET.fromstring(response.content)
            articles = []
            
            for item in root.findall(".//item")[:limit]:
                title = item.find("title").text if item.find("title") is not None else ""
                link = item.find("link").text if item.find("link") is not None else ""
                pub_date_str = item.find("pubDate").text if item.find("pubDate") is not None else ""
                
                # Parse RFC 2822 date format
                published_at = datetime.utcnow()
                if pub_date_str:
                    try:
                        published_at = parsedate_to_datetime(pub_date_str).replace(tzinfo=None)
                    except Exception:
                        pass

                articles.append({
                    "source": "Google News RSS",
                    "headline": title,
                    "content": title,  # RSS only gives titles in basic feeds
                    "url": link,
                    "published_at": published_at,
                    "ticker": ticker
                })
            return articles
        except Exception as e:
            logger.error(f"Google News RSS failed for {ticker}: {e}")
            return []


class YahooFinanceNewsProvider(NewsProvider):
    def __init__(self) -> None:
        self.client = httpx.AsyncClient(timeout=10.0)

    async def fetch_ticker_news(self, ticker: str, limit: int = 10) -> list[dict[str, Any]]:
        # Yahoo Finance Ticker RSS feed
        url = f"https://finance.yahoo.com/rss/headline?s={ticker}"
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            articles = []
            
            for item in root.findall(".//item")[:limit]:
                title = item.find("title").text if item.find("title") is not None else ""
                link = item.find("link").text if item.find("link") is not None else ""
                pub_date_str = item.find("pubDate").text if item.find("pubDate") is not None else ""
                description = item.find("description").text if item.find("description") is not None else ""

                published_at = datetime.utcnow()
                if pub_date_str:
                    try:
                        published_at = parsedate_to_datetime(pub_date_str).replace(tzinfo=None)
                    except Exception:
                        pass

                articles.append({
                    "source": "Yahoo Finance News",
                    "headline": title,
                    "content": description or title,
                    "url": link,
                    "published_at": published_at,
                    "ticker": ticker
                })
            return articles
        except Exception as e:
            logger.error(f"Yahoo Finance RSS failed for {ticker}: {e}")
            return []


class RedditApiProvider(NewsProvider):
    def __init__(self) -> None:
        self.client = httpx.AsyncClient(timeout=10.0)

    async def fetch_ticker_news(self, ticker: str, limit: int = 10) -> list[dict[str, Any]]:
        # Reddit REST query fallback stub.
        # Queries r/stocks or r/wallstreetbets search lists.
        # Requires User-Agent header (Reddit blocks empty user agents)
        headers = {"User-Agent": "AlphaForge/0.1.0"}
        url = f"https://www.reddit.com/r/stocks/search.json?q={ticker}&restrict_sr=1&sort=new&limit={limit}"
        try:
            response = await self.client.get(url, headers=headers)
            if response.status_code != 200:
                logger.warning(f"Reddit API returned code {response.status_code}. Using mock Reddit feed for {ticker}")
                return self._generate_mock_reddit(ticker, limit)
            
            data = response.json()
            children = data.get("data", {}).get("children", [])
            articles = []
            
            for child in children[:limit]:
                post_data = child.get("data", {})
                title = post_data.get("title", "")
                permalink = "https://www.reddit.com" + post_data.get("permalink", "")
                created_utc = post_data.get("created_utc")
                self_text = post_data.get("selftext", "")

                published_at = datetime.utcfromtimestamp(created_utc) if created_utc else datetime.utcnow()

                articles.append({
                    "source": "Reddit r/stocks",
                    "headline": title,
                    "content": self_text or title,
                    "url": permalink,
                    "published_at": published_at,
                    "ticker": ticker
                })
            return articles
        except Exception as e:
            logger.warning(f"Reddit API query encountered error: {e}. Fallback to simulated Reddit feed.")
            return self._generate_mock_reddit(ticker, limit)

    def _generate_mock_reddit(self, ticker: str, limit: int) -> list[dict[str, Any]]:
        posts = []
        now = datetime.utcnow()
        for idx in range(limit):
            posts.append({
                "source": "Reddit r/stocks (Simulated)",
                "headline": f"Is it time to accumulate more {ticker} before earnings?",
                "content": f"Looking at technical indicators and fundamentals, {ticker} appears to have solid momentum for Q3.",
                "url": f"https://reddit.com/r/stocks/mock_{ticker}_{idx}",
                "published_at": now - timedelta(hours=idx),
                "ticker": ticker
            })
        return posts

# Import timedelta inside providers to prevent errors
from datetime import timedelta
