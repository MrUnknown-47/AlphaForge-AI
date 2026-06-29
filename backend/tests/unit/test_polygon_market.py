import pytest
from app.modules.market_data.polygon_client import PolygonClient
from app.modules.market_data.websocket_client import PolygonWebsocketClient
from app.modules.market_data.cache import MarketDataCache
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_polygon_client_get_quote():
    client = PolygonClient()
    quote = await client.get_quote("AAPL")
    assert quote["symbol"] == "AAPL"
    assert "bid" in quote
    assert "ask" in quote

@pytest.mark.asyncio
async def test_polygon_client_get_snapshot():
    client = PolygonClient()
    snapshot = await client.get_snapshot("AAPL")
    assert "open" in snapshot
    assert "high" in snapshot

@pytest.mark.asyncio
async def test_polygon_client_get_bars():
    client = PolygonClient()
    bars = await client.get_bars("AAPL", "1d", "2026-06-01", "2026-06-10")
    assert len(bars) > 0
    assert "open" in bars[0]

@pytest.mark.asyncio
async def test_polygon_client_get_options_chain():
    client = PolygonClient()
    chain = await client.get_options_chain("AAPL")
    assert len(chain) > 0
    assert "strike" in chain[0]

@pytest.mark.asyncio
async def test_websocket_client_subscriptions():
    ws = PolygonWebsocketClient()
    await ws.connect()
    assert ws.active_connections == 1
    
    await ws.subscribe_quotes(["AAPL", "MSFT"])
    assert "Q.AAPL" in ws.subscription_registry
    assert "Q.MSFT" in ws.subscription_registry

    await ws.disconnect()
    assert ws.active_connections == 0

@pytest.mark.asyncio
async def test_market_cache_operations():
    cache = MarketDataCache()
    # Write to local cache / Redis
    cache.set("test_key", {"data": 123}, ttl=10)
    val = cache.get("test_key")
    assert val == {"data": 123}
