# Data Dictionary

This document maps the column names and database attributes of AlphaForge AI.

---

## 1. Tick Data Attributes
* `timestamp` (TIMESTAMPTZ): Partitioning key for TimescaleDB.
* `ticker` (VARCHAR(12)): Standard stock symbol.
* `close` (NUMERIC): Close transaction price in USD.
* `volume` (BIGINT): Aggregate shares traded in period.

---

## 2. Portfolio Risk Metrics
* `var` (NUMERIC): Value-at-Risk under 95% confidence intervals.
* `cvar` (NUMERIC): Conditional VaR expected shortfall.
* `leverage` (NUMERIC): Total gross assets divided by AUM.
