## Airframe (Starter) | An Airflow DAG Template

A simplified Airflow DAG template for BigQuery jobs.

## Features

- **Environment-based Configuration**: Automatically loads configuration from `config/{env}.yaml`, supporting `dev.yaml`/`development.yaml` and `prod.yaml`/`production.yaml`.
- **SQL Execution**: Executes external SQL files from the `sql/` directory.

## Configuration

Place your configuration files in the `config/` directory.

- `dev` env: checks `dev.yaml` or `development.yaml`
- `prod` env: checks `prod.yaml` or `production.yaml`
