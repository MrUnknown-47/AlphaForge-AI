# Derivatives Platform Engine

This document details the options and futures math, structures, and strategy parameters.

---

## 1. Options Models & Greeks Math
* **Black-Scholes-Merton Formulas:** Calculates Call and Put prices under standard geometric Brownian motion assumptions.
* **Option Greeks:**
  * **Delta (\(\Delta\)):** Sensitivity to underlying price shocks.
  * **Gamma (\(\Gamma\)):** Sensitivity of Delta to underlying price shocks.
  * **Vega:** Sensitivity to volatility shifts.
  * **Theta (\(\Theta\)):** Option premium decay over time.

---

## 2. Options Strategy Configurations
Supports covered calls, cash secured puts, iron condors, iron butterflies, calendars, and vertical spreads calculation.

---

## 3. Futures Strategy Configurations
Provides calendar spread basis trading, carry trading yield estimations, and exposure hedging contract roundings.
