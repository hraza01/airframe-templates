## Airframe (Standard) | An Airflow DAG Template

A standard Airflow DAG template for BigQuery jobs with advanced SQL templating.

## Features

- **Environment-based Configuration**: Automatically loads configuration from `config/{env}.yaml`, supporting `dev.yaml`/`development.yaml` and `prod.yaml`/`production.yaml`.
- **Advanced SQL Templating**: Supports Jinja2 macros and looping (see `sql/star-wars.sql`).
- **BigQuery Integration**: Executes queries directly using `BigQueryInsertJobOperator`.

## Configuration

Place your configuration files in the `config/` directory.

- `dev` env: checks `dev.yaml` or `development.yaml`
- `prod` env: checks `prod.yaml` or `production.yaml`

## SQL Templating

The template demonstrates how to use Jinja2 for dynamic query generation:

- `{% include %}` for modular SQL
- `{% for %}` loops for repetitive structures (e.g., UNION ALL)
- Custom macros (partials) (in `sql/templates/`)
