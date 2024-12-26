# Default target
.PHONY: setup
setup:
	@echo "Checking for Poetry installation..."
	@command -v poetry >/dev/null 2>&1 || { echo >&2 "Poetry is not installed. Please install it: https://python-poetry.org/docs/#installation"; exit 1; }
	@echo "Setting up environment with Poetry..."
	poetry install

.PHONY: activate
activate:
	@echo "Activating Poetry virtual environment..."
	poetry shell
