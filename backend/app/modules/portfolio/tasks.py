# Background tasks for the Portfolio module operations

def take_portfolio_snapshot_daily() -> None:
    """
    Scheduled task that records close-of-market NAV and holdings allocation snapshots
    for all active portfolios to feed historical performance charts.
    """
    pass

def calculate_portfolio_ratios_hourly() -> None:
    """
    Computes Sharpe, Sortino, and Volatility values for portfolios by aggregating
    historical valuation points from database tables.
    """
    pass