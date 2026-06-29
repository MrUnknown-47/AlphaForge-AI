from typing import Dict, Any

class BenchmarkEngine:
    def __init__(self) -> None:
        self.benchmark_returns = {
            "SPY": 0.085, # 8.5% benchmark return
            "QQQ": 0.124,
            "ACWI": 0.062
        }

    def get_alpha_vs_benchmark(self, benchmark: str, portfolio_return: float) -> float:
        bench_ret = self.benchmark_returns.get(benchmark.upper(), 0.08)
        return float(portfolio_return - bench_ret)
