import logging
import numpy as np
import pandas as pd
from typing import Any

logger = logging.getLogger(__name__)

try:
    import shap
    HAS_SHAP = True
except Exception as e:
    HAS_SHAP = False
    logger.warning(f"shap could not be loaded: {e}. Falling back to standard importance.")

class FeatureExplainer:
    def calculate_shap_values(self, trained_model: Any, X_train: np.ndarray, feature_names: list[str]) -> dict[str, float]:
        """
        Computes SHAP feature importance.
        Returns a dict mapping feature names to their absolute mean SHAP importance.
        """
        if HAS_SHAP:
            try:
                explainer = shap.TreeExplainer(trained_model)
                shap_values = explainer.shap_values(X_train)
                
                if isinstance(shap_values, list):
                    shap_values = np.mean([np.abs(v) for v in shap_values], axis=0)
                else:
                    shap_values = np.abs(shap_values)

                mean_shap = np.mean(shap_values, axis=0)
                return {name: float(val) for name, val in zip(feature_names, mean_shap)}
            except Exception as e:
                logger.warning(f"SHAP explainer failed: {e}. Falling back to standard importance.")
                return self._calculate_fallback_importance(trained_model, feature_names)
        else:
            return self._calculate_fallback_importance(trained_model, feature_names)

    def _calculate_fallback_importance(self, model: Any, feature_names: list[str]) -> dict[str, float]:
        inner_model = getattr(model, "model", None) or model
        if hasattr(inner_model, "feature_importances_"):
            importances = inner_model.feature_importances_
            return {name: float(val) for name, val in zip(feature_names, importances)}
        
        num_features = len(feature_names)
        return {name: float(1.0 / num_features) for name in feature_names}

    def generate_feature_rankings(self, importances: dict[str, float]) -> list[dict[str, Any]]:
        """Sorts features by importance to construct ranking lists."""
        sorted_feats = sorted(importances.items(), key=lambda x: x[1], reverse=True)
        return [{"rank": idx + 1, "feature": name, "importance": val} for idx, (name, val) in enumerate(sorted_feats)]

    def calculate_partial_dependence(
        self, model: Any, X: np.ndarray, feature_index: int, grid_resolution: int = 10
    ) -> list[dict[str, float]]:
        """
        Computes 1D Partial Dependence values for a feature index.
        Calculates average model prediction when the target feature values are forced across a grid range.
        """
        feature_vals = X[:, feature_index]
        grid = np.linspace(np.min(feature_vals), np.max(feature_vals), grid_resolution)
        
        pdp_values = []
        X_temp = X.copy()
        
        for val in grid:
            # Force the feature column to the grid value
            X_temp[:, feature_index] = val
            preds = model.predict(X_temp)
            mean_pred = float(np.mean(preds))
            pdp_values.append({"value": float(val), "average_prediction": mean_pred})
            
        return pdp_values

    def calculate_psi(self, expected: np.ndarray, actual: np.ndarray, num_buckets: int = 10) -> float:
        """
        Computes Population Stability Index (PSI) to track feature drift.
        PSI < 0.1: No significant drift.
        PSI 0.1 - 0.25: Moderate drift.
        PSI > 0.25: Significant drift.
        """
        try:
            # Check empty inputs
            if len(expected) == 0 or len(actual) == 0:
                return 0.0

            # Calculate quantiles on expected distribution
            percentiles = np.linspace(0, 100, num_buckets + 1)
            buckets = np.percentile(expected, percentiles)
            # Adjust endpoints to handle boundaries
            buckets[0] -= 1e-5
            buckets[-1] += 1e-5

            # Compute frequencies
            expected_counts, _ = np.histogram(expected, bins=buckets)
            actual_counts, _ = np.histogram(actual, bins=buckets)

            # Convert to percentages
            expected_pct = expected_counts / len(expected)
            actual_pct = actual_counts / len(actual)

            # Prevent zero counts causing division by zero or log(0) issues
            expected_pct = np.where(expected_pct == 0, 0.0001, expected_pct)
            actual_pct = np.where(actual_pct == 0, 0.0001, actual_pct)

            # Compute PSI formula
            psi_value = np.sum((actual_pct - expected_pct) * np.log(actual_pct / expected_pct))
            return float(psi_value)
        except Exception as e:
            logger.error(f"Failed to calculate PSI feature drift: {e}")
            return 0.0
