.PHONY: format check lint fix help

help:
	@echo "Available commands:"
	@echo "  make format  - Format all Python files with ruff"
	@echo "  make check   - Check formatting without making changes"
	@echo "  make lint    - Run linting checks"
	@echo "  make fix     - Auto-fix linting issues where possible"

format:
	ruff format .

check:
	ruff format --check .

lint:
	ruff check .

fix:
	ruff check --fix .
