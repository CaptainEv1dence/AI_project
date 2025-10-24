PYTHON_VERSION := 3.12
VENV ?= .venv

.create-venv:
	test -d $(VENV) || python$(PYTHON_VERSION) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install poetry

init: .create-venv
	$(VENV)/bin/python -m pip install toml
	$(VENV)/bin/poetry install

api:
	$(VENV)/bin/python -m uvicorn backend.main:app --reload --port 8000

# Test commands
install-test:
	$(VENV)/bin/pip install pytest pytest-cov httpx

test:
	$(VENV)/bin/pytest backend/tests/ -v

test-cov:
	$(VENV)/bin/pytest backend/tests/ -v --cov=backend --cov-report=term-missing

.PHONY: init api install-test test test-cov
