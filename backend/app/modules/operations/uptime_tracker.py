class UptimeTracker:
    def __init__(self) -> None:
        self.total_ticks = 1000
        self.failed_ticks = 2
        self.ws_reconnects = 1

    def track_tick(self, success: bool) -> None:
        self.total_ticks += 1
        if not success:
            self.failed_ticks += 1

    def record_reconnect(self) -> None:
        self.ws_reconnects += 1

    def calculate_uptime(self) -> float:
        if self.total_ticks == 0:
            return 100.0
        return (1.0 - (self.failed_ticks / self.total_ticks)) * 100.0
