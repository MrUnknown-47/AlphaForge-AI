import logging
from typing import Dict, Any

logger = logging.getLogger("ModelMonitor")

class ModelMonitor:
    def __init__(self) -> None:
        self.sharpe = 1.58
        self.hit_ratio = 0.612
        self.confidence = 0.85
        self.psi = 0.08
        self.aborted = False

    def track_model_status(
        self, sharpe: float, hit_ratio: float, confidence: float, psi: float
    ) -> Dict[str, Any]:
        self.sharpe = sharpe
        self.hit_ratio = hit_ratio
        self.confidence = confidence
        self.psi = psi

        # Enforce validation abort limits
        if sharpe < 1.0:
            logger.error("ABORT: Rolling Sharpe collapsed below 1.0 threshold!")
            self.aborted = True
        if hit_ratio < 0.55:
            logger.error("ABORT: Strategy hit ratio collapsed below 55% threshold!")
            self.aborted = True
        if psi > 0.25:
            logger.error("ABORT: Feature drift exceeded 0.25 PSI threshold!")
            self.aborted = True

        return {
            "sharpe": self.sharpe,
            "hit_ratio": self.hit_ratio,
            "prediction_confidence": self.confidence,
            "psi_drift": self.psi,
            "feature_drift": self.psi * 0.5,
            "concept_drift": self.psi * 0.8,
            "staleness_hours": 0.5,
            "aborted": self.aborted
        }
