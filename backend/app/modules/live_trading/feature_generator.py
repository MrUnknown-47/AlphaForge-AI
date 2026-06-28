import numpy as np
import pandas as pd
from typing import Dict, List

class FeatureGenerator:
    def __init__(self) -> None:
        self.approved_features = [
            "returns_1d", "returns_5d", "returns_20d", "realized_vol_20", "ATR14",
            "RSI14", "MACD", "Bollinger width", "EMA10", "EMA200", "market_beta",
            "SPY correlation", "QQQ correlation", "PE", "PB", "ROE", "debt_to_equity",
            "sentiment_mean", "sentiment_change"
        ]

    def compute_features(self, history: pd.DataFrame) -> pd.DataFrame:
        """
        Receives raw history pricing dataframe and computes the 19 high-conviction features.
        - history must contain: 'close', 'high', 'low', 'open', 'volume', 'spy_close', 'qqq_close',
          'pe', 'pb', 'roe', 'debt_to_equity', 'sentiment_mean'
        """
        df = history.copy()
        
        # 1. Returns
        df["returns_1d"] = df["close"].pct_change(1)
        df["returns_5d"] = df["close"].pct_change(5)
        df["returns_20d"] = df["close"].pct_change(20)

        # 2. Volatility
        df["realized_vol_20"] = df["returns_1d"].rolling(20).std() * np.sqrt(252)
        
        # ATR14 (Average True Range)
        high_low = df["high"] - df["low"]
        high_close = (df["high"] - df["close"].shift()).abs()
        low_close = (df["low"] - df["close"].shift()).abs()
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        df["ATR14"] = tr.rolling(14).mean()

        # 3. Momentum (RSI14)
        delta = df["close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / (loss + 1e-8)
        df["RSI14"] = 100 - (100 / (1 + rs))

        # 4. Trend (EMA10, EMA200, MACD)
        df["EMA10"] = df["close"].ewm(span=10, adjust=False).mean()
        df["EMA200"] = df["close"].ewm(span=200, adjust=False).mean()
        df["MACD"] = df["close"].ewm(span=12, adjust=False).mean() - df["close"].ewm(span=26, adjust=False).mean()

        # Bollinger Bands Width
        sma20 = df["close"].rolling(20).mean()
        std20 = df["close"].rolling(20).std()
        df["Bollinger width"] = (4 * std20) / (sma20 + 1e-8)

        # 5. Regime (SPY/QQQ Correlation, Market Beta)
        df["spy_returns"] = df["spy_close"].pct_change(1)
        df["qqq_returns"] = df["qqq_close"].pct_change(1)
        df["SPY correlation"] = df["returns_1d"].rolling(20).corr(df["spy_returns"])
        df["QQQ correlation"] = df["returns_1d"].rolling(20).corr(df["qqq_returns"])
        
        # Market Beta
        cov = df["returns_1d"].rolling(20).cov(df["spy_returns"])
        var = df["spy_returns"].rolling(20).var()
        df["market_beta"] = cov / (var + 1e-8)

        # 6. Fundamentals & Sentiment (Fill/copy existing keys)
        df["PE"] = df.get("pe", 20.0).ffill().fillna(20.0)
        df["PB"] = df.get("pb", 3.0).ffill().fillna(3.0)
        df["ROE"] = df.get("roe", 0.15).ffill().fillna(0.15)
        df["debt_to_equity"] = df.get("debt_to_equity", 0.5).ffill().fillna(0.5)
        
        df["sentiment_mean"] = df.get("sentiment_mean", 0.1).ffill().fillna(0.1)
        df["sentiment_change"] = df["sentiment_mean"].diff().fillna(0.0)

        # Select only the 19 approved high-conviction features
        df_feats = df[self.approved_features].copy()
        # Clean any remaining NaNs via rolling mean/ffill
        df_feats = df_feats.ffill().bfill().fillna(0.0)
        
        return df_feats
