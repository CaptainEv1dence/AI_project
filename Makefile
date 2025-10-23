PYTHON_VERSION := 3.12
VENV ?= .venv

.create-venv:
	test -d $(VENV) || python$(PYTHON_VERSION) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install poetry

init: .create-venv
	$(VENV)/bin/python -m pip install toml
	$(VENV)/bin/poetry install
