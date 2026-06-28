import logging
from typing import Dict, Any

logger = logging.getLogger("SchedulerMonitor")

class SchedulerMonitor:
    def __init__(self) -> None:
        self.success_count = 100
        self.failure_count = 0

    def log_run(self, success: bool) -> None:
        if success:
            self.success_count += 1
        else:
            self.failure_count += 1
            logger.error("Scheduler execution failed!")

    def get_stats(self) -> Dict[str, Any]:
        total = self.success_count + self.failure_count
        rate = (self.success_count / total) * 100.0 if total > 0 else 100.0
        return {
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "execution_success_rate": rate
        }
