## Airframe (Advanced) | An Airflow DAG Template

## Code Formatting

This DAG uses [Ruff](https://docs.astral.sh/ruff/) for code formatting and linting enforcement.

### Installation

```bash
# Install ruff globally (recommended)
$ uv tool install ruff

# OR install in your virtual environment at the root of your project
# i.e. composer/<your-airflow-env>/.venv
$ pip install ruff
```

### Usage

#### Using Makefile (Recommended)

```bash
# Format all Python files
$ make format

# Check formatting without making changes
$ make check

# Run linting checks
$ make lint

# Auto-fix linting issues
$ make fix
```

#### Using Ruff Directly

```bash
# Format all Python files in this folder
$ ruff format .

# Check formatting
$ ruff format --check .

# Run linting
$ ruff check .

# Auto-fix linting issues
$ ruff check --fix .
```

### Pre-commit Hooks (Recommended)

To automatically enforce formatting on every commit:

```bash
# Install pre-commit globally (recommended - one-time setup)
$ uv tool install pre-commit

# OR install in your virtual environment at the root of your project
# i.e. composer/<your-airflow-env>/.venv
$ pip install pre-commit

# Navigate to the DAG folder and install git hooks
$ cd dags/advanced
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit

# Run manually (optional - to check all files)
$ pre-commit run --all-files
ruff.....................................................................Passed
ruff-format..............................................................Passed
```

> **Note:** Installing with `uv tool install pre-commit` makes pre-commit available globally across all your projects. You only need to run `pre-commit install` once per DAG folder to enable the hooks.

### Configuration

Ruff is configured via [pyproject.toml](./pyproject.toml) in this folder. You can customize:

- Line length (currently 120)
- Linting rules
- Code style preferences

### CI/CD Integration

Add this to your CI/CD pipeline:

```bash
# In the dags/advanced/ directory
$ cd dags/advanced
$ ruff format --check .
$ ruff check .
```

Example GitHub Actions workflow:

```yaml
name: Code Quality

on: [push, pull_request]

jobs:
    lint:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v4

            - name: Install ruff
              run: pip install ruff

            - name: Check formatting
              run: |
                  cd dags/advanced
                  ruff format --check .
                  ruff check .
```
