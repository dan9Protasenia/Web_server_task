# Env setup
py := poetry run
python := $(py) python -m
main_dir := src
test_dir := tests

code_dir = $(main_dir) $(test_dir)


# Info
.PHONY: default
default:
	@echo I\'m default command if you run \'Make\' without any additional args...


# Docker build and run
.PHONY: sync-up async-up

## Sync
sync-up: sync-build sync-run

sync-build:
	docker build -t sync-app -f src/app/sync_main/Dockerfile .

sync-run:
	docker run -p 8001:8001 sync-app

## Async
async-up: sync-build sync-run

async-build:
	docker build -t async-app -f src/app/async_main/Dockerfile .

async-run:
	docker run -p 8002:8002 async-app


# Local
## Sync
.PHONY: sync-up async-up

sync-launch:
	$(python) src.app.sync.main

async-launch:
	$(python) src.app.async_main.main


# Run tests with pytest
.PHONY: test

test:
	$(py) pytest  # ToDo: any flags (add in `pyproject.toml`)? If how have containerezied app you also need to launch tests in contaers, e.g. for launch them on github side as a pipeline workflow


# Project cleaner & Linters
.PHONY: clean lint

clean:
	@-find . -name \*__pycache__ -type d -exec rm -rf '{}' \;
	@-find . -name \*.pytest_cache -type d -exec rm -rf '{}' \;
	@-find . -name \*.mypy_cache -type d -exec rm -rf '{}' \;

lint:
	@-$(py) isort $(code_dir)
	@-$(py) black $(code_dir)
	@-$(py) flake8 $(code_dir)
	@-$(py) mypy $(code_dir)
