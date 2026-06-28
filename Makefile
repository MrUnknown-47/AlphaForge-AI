# --- Configurations ---
COMPOSE_FILE=infra/docker-compose.yml

.PHONY: init build up up-d down restart logs shell-backend shell-db migrate migration lint format clean

# Initialize local environment
init:
	cp .env.example .env
	pre-commit install || echo "Pre-commit hooks installation skipped (pre-commit not found on host)"

# Build docker containers
build:
	docker compose -f $(COMPOSE_FILE) build

# Start containers in foreground
up:
	docker compose -f $(COMPOSE_FILE) up

# Start containers in background
up-d:
	docker compose -f $(COMPOSE_FILE) up -d

# Stop and remove containers, preserving volumes
down:
	docker compose -f $(COMPOSE_FILE) down

# Restart container services
restart:
	docker compose -f $(COMPOSE_FILE) restart

# Stream container logs
logs:
	docker compose -f $(COMPOSE_FILE) logs -f

# SSH into the running backend container
shell-backend:
	docker compose -f $(COMPOSE_FILE) exec backend /bin/bash

# Open psql terminal inside running database container
shell-db:
	docker compose -f $(COMPOSE_FILE) exec db psql -U postgres -d alphaforge

# Run alembic migrations
migrate:
	docker compose -f $(COMPOSE_FILE) exec backend alembic upgrade head

# Generate a new alembic migration (Usage: make migration msg="migration_name")
migration:
	docker compose -f $(COMPOSE_FILE) exec backend alembic revision --autogenerate -m "$(msg)"

# Run linting checks inside backend container
lint:
	docker compose -f $(COMPOSE_FILE) exec backend ruff check app/
	docker compose -f $(COMPOSE_FILE) exec backend mypy app/

# Run code formatters
format:
	docker compose -f $(COMPOSE_FILE) exec backend black app/
	docker compose -f $(COMPOSE_FILE) exec backend ruff check --fix app/

# Remove docker containers, images, volumes, and dangling items
clean:
	docker compose -f $(COMPOSE_FILE) down -v --rmi all
	docker system prune -f