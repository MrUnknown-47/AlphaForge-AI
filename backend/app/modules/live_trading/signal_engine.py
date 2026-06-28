import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple

class SignalEngine:
    def __init__(self, models: Dict[str, Dict[str, Any]]) -> None:
        self.models = models
        self.buy_threshold = 0.012  # Expecting > 1.2% return
        self.sell_threshold = -0.012

    def calculate_ensemble_prediction(self, features_df: pd.DataFrame) -> Tuple[float, float, float]:
        """Computes predictions for XGBoost and LSTM and returns ensemble prediction."""
        # Extract features array (last row representing current state)
        last_row = features_df.iloc[[-1]].copy()
        
        preds = {}
        for key in ["xgboost", "lstm"]:
            if key in self.models:
                m_data = self.models[key]
                model = m_data["model"]
                scaler = m_data["scaler"]
                feats_list = m_data["features"]
                
                # Align features schema
                for f_name in feats_list:
                    if f_name not in last_row.columns:
                        last_row[f_name] = 0.0
                aligned_row = last_row[feats_list]
                scaled_feats = scaler.transform(aligned_row)
                
                pred_val = model.predict(scaled_feats)
                if isinstance(pred_val, np.ndarray):
                    pred_val = float(pred_val.item())
                preds[key] = float(pred_val)
            else:
                preds[key] = 0.0

        xg_pred = preds.get("xgboost", 0.0)
        lstm_pred = preds.get("lstm", 0.0)
        
        # Approved ensemble weighting: 0.7 XGBoost + 0.3 LSTM
        ensemble_pred = (0.7 * xg_pred) + (0.3 * lstm_pred)
        return xg_pred, lstm_pred, ensemble_pred

    def generate_signal(self, ensemble_pred: float) -> str:
        """Translates predictions to BUY, SELL, or HOLD signals."""
        if ensemble_pred > self.buy_threshold:
            return "BUY"
        elif ensemble_pred < self.sell_threshold:
            return "SELL"
        return "HOLD"
