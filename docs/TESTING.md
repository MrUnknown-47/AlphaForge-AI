# AlphaForge AI Test & Verification Suite

This document describes the testing frameworks and verification commands.

---

## 1. Test Command Suite

1. **Unit & Integration Suite (Pytest):**
```bash
pytest backend/tests/
```
2. **Coverage Checks:**
```bash
pytest --cov=backend/app backend/tests/
```

---

## 2. Test Architecture Categories

1. **Backend Integration Tests:** Exercises JWT validations, database CRUD interfaces, and router prefixes.
2. **Backtesting Laboratory Tests:** Validates WFO (Walk-Forward Optimization) metrics and data alignment.
3. **MFA TOTP Validation Checks:** Simulates cryptographically sound MFA code validations.
4. **Operations Incident Logs Checks:** Asserts P0 incident dispatch logs metrics.
