# AlphaForge AI API Documentation

This document describes the API endpoints exposed by the AlphaForge AI backend services.

---

## 1. Authentication Service
* **Endpoint:** `/auth/login`
* **Method:** `POST`
* **Auth Requirement:** None
* **Request Schema:**
  ```json
  {
    "username": "quant_trader",
    "password": "securepassword"
  }
  ```
* **Response Schema (200 OK):**
  ```json
  {
    "access_token": "eyJhbGciOi...",
    "token_type": "bearer",
    "role": "TRADER"
  }
  ```

---

## 2. Prediction Engine
* **Endpoint:** `/prediction/signal`
* **Method:** `GET`
* **Auth Requirement:** JWT Bearer
* **Response Schema (200 OK):**
  ```json
  {
    "ticker": "AAPL",
    "probability": 0.76,
    "signal": "BUY",
    "timestamp": "2026-06-28T14:35:00Z"
  }
  ```

---

## 3. Portfolio Manager
* **Endpoint:** `/portfolio/allocation`
* **Method:** `POST`
* **Auth Requirement:** JWT (Role: ADMIN/TRADER)
* **Request Schema:**
  ```json
  {
    "method": "HRP"
  }
  ```
* **Response Schema (200 OK):**
  ```json
  {
    "status": "ALLOCATED",
    "weights": {
      "AAPL": 0.28,
      "NVDA": 0.30,
      "MSFT": 0.25,
      "TSLA": 0.17
    }
  }
  ```
