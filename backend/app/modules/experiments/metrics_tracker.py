from typing import List

class MetricsTracker:
    def __init__(self) -> None:
        self.metrics_history: List[float] = []

    def log_metric(self, value: float) -> None:
        self.metrics_history.append(value)

    def get_history(self) -> List[float]:
        return self.metrics_history
