from typing import Dict, Any

class MetricsCollector:
    def __init__(self) -> None:
        self.collected_metrics = {}

    def collect(self, name: str, metrics: Dict[str, Any]) -> None:
        self.collected_metrics[name] = metrics

    def get_summary(self) -> Dict[str, Any]:
        return self.collected_metrics
