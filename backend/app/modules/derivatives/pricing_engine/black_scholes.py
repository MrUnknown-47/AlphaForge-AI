import numpy as np
from scipy.stats import norm

def call_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
    if T <= 0:
        return max(S - K, 0.0)
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def put_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
    if T <= 0:
        return max(K - S, 0.0)
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def implied_volatility(price: float, S: float, K: float, T: float, r: float, option_type: str = "CALL") -> float:
    # Newton-Raphson method
    sigma = 0.3 # initial guess
    for _ in range(100):
        if option_type.upper() == "CALL":
            diff = call_price(S, K, T, r, sigma) - price
        else:
            diff = put_price(S, K, T, r, sigma) - price
        
        if abs(diff) < 1e-6:
            return sigma
        
        v = vega(S, K, T, r, sigma) * 100.0
        if v < 1e-6:
            break
        sigma -= diff / v
        sigma = max(0.001, min(sigma, 5.0)) # boundary guards
    return sigma

def delta(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "CALL") -> float:
    if T <= 0:
        if option_type.upper() == "CALL":
            return 1.0 if S > K else 0.0
        else:
            return -1.0 if S < K else 0.0
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type.upper() == "CALL":
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1.0

def gamma(S: float, K: float, T: float, r: float, sigma: float) -> float:
    if T <= 0 or sigma <= 0:
        return 0.0
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def theta(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "CALL") -> float:
    if T <= 0:
        return 0.0
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    first_term = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    if option_type.upper() == "CALL":
        second_term = r * K * np.exp(-r * T) * norm.cdf(d2)
        return (first_term - second_term) / 365.0 # daily theta
    else:
        second_term = r * K * np.exp(-r * T) * norm.cdf(-d2)
        return (first_term + second_term) / 365.0 # daily theta

def vega(S: float, K: float, T: float, r: float, sigma: float) -> float:
    if T <= 0:
        return 0.0
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * np.sqrt(T) * norm.pdf(d1) / 100.0 # 1% change

def rho(S: float, K: float, T: float, r: float, sigma: float, option_type: str = "CALL") -> float:
    if T <= 0:
        return 0.0
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type.upper() == "CALL":
        return K * T * np.exp(-r * T) * norm.cdf(d2) / 100.0 # 1% change
    else:
        return -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100.0 # 1% change
