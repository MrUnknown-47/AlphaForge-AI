from decimal import Decimal

class PortfolioCalculator:
    def calculate_nav(self, cash: Decimal, holdings: list[dict], prices: dict[str, Decimal]) -> Decimal:
        """
        Formula: NAV = Cash + Sum(Position_i * Price_i)
        """
        holdings_value = Decimal("0.0")
        for holding in holdings:
            ticker = holding["ticker"]
            qty = Decimal(str(holding["quantity"]))
            price = prices.get(ticker, Decimal("0.0"))
            holdings_value += qty * price
        return cash + holdings_value

    def calculate_returns(self, nav_history: list[Decimal]) -> list[float]:
        returns = []
        for i in range(1, len(nav_history)):
            prev = nav_history[i-1]
            curr = nav_history[i]
            if prev > 0:
                ret = float((curr - prev) / prev)
                returns.append(ret)
        return returns

class MetricsCalculator:
    def calculate_sharpe_ratio(self, returns: list[float], risk_free_rate: float = 0.02) -> float:
        # Standard Sharpe formula skeleton: (mean_return - risk_free) / volatility
        return 1.5  # Stub value representation

    def calculate_sortino_ratio(self, returns: list[float], target_return: float = 0.0) -> float:
        # Sortino formula: (mean_return - target_return) / downside_deviation
        return 1.8  # Stub value representation

    def calculate_max_drawdown(self, nav_history: list[Decimal]) -> float:
        # Peak-to-trough drop calculation stub
        return 0.12  # 12% Max drawdown stub

class RiskCalculator:
    def calculate_beta(self, portfolio_returns: list[float], benchmark_returns: list[float]) -> float:
        # Formula: Covariance(Rp, Rm) / Variance(Rm)
        return 1.1  # Aggressive beta stub representation

    def calculate_alpha(self, portfolio_return: float, beta: float, market_return: float, risk_free: float = 0.02) -> float:
        # CAPM Alpha formula: Rp - [Rf + Beta * (Rm - Rf)]
        return 0.04  # 4% Alpha stub representation
