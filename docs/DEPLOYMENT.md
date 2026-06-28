# AlphaForge AI Production Deployment Guide

This document contains standard operational templates and deployment steps.

---

## 1. Docker Compose (Staging/Local)

To run a fully containerized environment:
```yaml
version: "3.8"
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: securepassword
  redis:
    image: redis:7
  backend:
    build: ./backend
    ports:
      - "8000:8000"
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
```

Run compose:
```bash
docker compose up --build -d
```

---

## 2. Production Rollback Steps
If telemetry alerts detect error rate spike (> 1%) on deployment:
1. Revert container image tags:
```bash
kubectl set image deployment/alphaforge-backend backend=registry.internal/backend:v1.0.0-previous
```
2. Verify liveness heartbeats:
```bash
kubectl rollout status deployment/alphaforge-backend
```
