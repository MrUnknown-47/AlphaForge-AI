import pandas as pd
import numpy as np

def calculate_rolling_mean(series: pd.Series, window: int = 20) -> pd.Series:
    return series.rolling(window=window, min_periods=1).mean()

def calculate_rolling_std(series: pd.Series, window: int = 20) -> pd.Series:
    # Fill standard deviation with 0 if variance is zero
    std = series.rolling(window=window, min_periods=1).std()
    return std.fillna(0.0)

def calculate_zscore(series: pd.Series, window: int = 20) -> pd.Series:
    mean = calculate_rolling_mean(series, window)
    std = calculate_rolling_std(series, window)
    
    # Avoid zero standard deviation division leading to inf/NaN values
    diff = series - mean
    return diff / np.where(std == 0, 1e-8, std)

def calculate_returns(series: pd.Series, lag: int = 1) -> pd.Series:
    return series.pct_change(periods=lag).fillna(0.0)

def calculate_rolling_volatility(returns: pd.Series, window: int = 20) -> pd.Series:
    # Volatility = Standard deviation of returns * sqrt(252) (if daily annualized)
    # We return the simple standard deviation across the window for this MVP
    return returns.rolling(window=window, min_periods=1).std().fillna(0.0)
