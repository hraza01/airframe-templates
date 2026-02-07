# Barebones Template

A barebones template for Airflow DAGs.

## Features

- **Environment-based Configuration**: Automatically loads configuration from `config/{env}.yaml`, supporting `dev.yaml`/`development.yaml` and `prod.yaml`/`production.yaml`.

## Configuration

Place your configuration files in the `config/` directory.

- `dev` env: checks `dev.yaml` or `development.yaml`
- `prod` env: checks `prod.yaml` or `production.yaml`
