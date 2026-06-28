# AlphaForge AI Security Framework

This document outlines the security controls, governance policies, and safety guardrails.

---

## 1. Authentication & Session Security

1. **JSON Web Tokens (JWT):** Short-lived access tokens (30 minutes expiry) coupled with cryptographically signed refresh tokens.
2. **Multi-Factor Authentication (MFA):** Authenticator app TOTP validation required for TRADER and ADMIN role elevations.
3. **Session Auto-Lock:** Session terminates automatically after 15 minutes of user inactivity.

---

## 2. Hardened Risk Controls

1. **Capital Guard Limits:** Rigid bounds enforcing:
   * Maximum individual position exposure (e.g. 5% AUM).
   * Daily loss limits.
   * Maximum drawdown limit triggers.
2. **Emergency Kill Switch:** A multi-role endpoint to halt all active executions and liquidate open positions globally.
3. **AI Copilot Boundaries:** Strict observational-only policies. AI recommendations are entirely segregated from execution pathways.
