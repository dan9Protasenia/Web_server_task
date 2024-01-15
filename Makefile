# Makefile

# Docker commands for asynchronous server
ASYNC_BUILD = docker build -t async-app -f src/async_main/Dockerfile src/async_main
ASYNC_RUN = docker run -p 8002:8002 async-app

# Docker commands for synchronous server
SYNC_BUILD = docker build -t sync-app -f src/sync/Dockerfile src/sync
SYNC_RUN = docker run -p 8001:8001 sync-app

# Poetry commands for running the servers
POETRY_RUN_ASYNC = poetry run python src/async_main/main.py
POETRY_RUN_SYNC = poetry run python src/sync/main.py

.PHONY: build-async run-async build-sync run-sync run-poetry-async run-poetry-sync

# Build Docker images
build-async:
	$(ASYNC_BUILD)

build-sync:
	$(SYNC_BUILD)

# Run Docker containers
run-async:
	$(ASYNC_RUN)

run-sync:
	$(SYNC_RUN)

# Run servers with poetry
run-poetry-async:
	$(POETRY_RUN_ASYNC)

run-poetry-sync:
	$(POETRY_RUN_SYNC)

# Combined build and run commands
start-async: build-async run-async
start-sync: build-sync run-sync

# Highlighted poetry run commands
start-poetry-async:
	@echo "Starting the asynchronous server with poetry..."
	@$(POETRY_RUN_ASYNC)

start-poetry-sync:
	@echo "Starting the synchronous server with poetry..."
	@$(POETRY_RUN_SYNC)

# Run tests with pytest
test:
	poetry run pytest

# Check code style with flake8
lint:
	poetry run flake8

# Format code with isort
format:
	poetry run isort .

.PHONY: lint format
