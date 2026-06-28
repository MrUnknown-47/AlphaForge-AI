class DriftMonitor:
    def __init__(self) -> None:
        self.psi = 0.08

    def check_drift(self) -> float:
        return self.psi
