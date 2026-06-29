import pytest
from app.modules.portfolio.analytics import (
    calculate_volatility,
    calculate_sharpe,
    calculate_sortino,
    calculate_max_drawdown,
    calculate_beta
)
from app.modules.portfolio.risk import (
    calculate_var,
    calculate_cvar,
    calculate_leverage,
    calculate_concentration
)
from app.modules.portfolio.exposure import calculate_exposure, calculate_sector_weights
from app.modules.portfolio.attribution import sector_contribution

@pytest.mark.asyncio
async def test_analytics_metrics():
    returns = [0.01, -0.02, 0.015, 0.005, -0.01]
    
    vol = calculate_volatility(returns)
    assert vol >= 0.0
    
    sharpe = calculate_sharpe(returns)
    assert isinstance(sharpe, float)
    
    sortino = calculate_sortino(returns)
    assert isinstance(sortino, float)
    
    max_dd = calculate_max_drawdown([100.0, 105.0, 95.0, 102.0, 90.0])
    assert max_dd == pytest.approx(0.1428, abs=1e-3) # Drawdown from 105 to 90 is 15/105 = 0.1428

@pytest.mark.asyncio
async def test_risk_metrics():
    returns = [0.01, -0.02, 0.015, 0.005, -0.01, 0.02, -0.005, 0.012, -0.015, 0.008]
    
    var_val = calculate_var(returns, 0.95)
    cvar_val = calculate_cvar(returns, 0.95)
    
    assert var_val >= 0.0
    assert cvar_val >= var_val
    
    lev = calculate_leverage(equity=100000.0, portfolio_value=150000.0)
    assert lev == 1.5

@pytest.mark.asyncio
async def test_exposure_and_contributions():
    positions = [
        {"symbol": "AAPL", "quantity": 10, "avg_price": 150.0, "market_price": 160.0, "market_value": 1600.0, "unrealized_pnl": 100.0, "unrealized_pct": 0.0667},
        {"symbol": "TSLA", "quantity": 5, "avg_price": 200.0, "market_price": 190.0, "market_value": 950.0, "unrealized_pnl": -50.0, "unrealized_pct": -0.05}
    ]
    cash = 2450.0 # Total assets = 1600 + 950 + 2450 = 5000
    
    exp = calculate_exposure(positions, cash)
    assert exp == 0.51 # (1600 + 950) / 5000
    
    sectors = calculate_sector_weights(positions, cash)
    assert sectors["Technology"] == 0.32 # 1600 / 5000
    assert sectors["Consumer Cyclical"] == 0.19 # 950 / 5000
    
    contribs = sector_contribution(positions, 0.02)
    assert "Technology" in contribs
