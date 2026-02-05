"""
Utility functions for Airflow DAG operations.

This module provides helper functions for loading configuration and documentation files.
"""

from pathlib import Path


def load_workflow_md() -> str:
    """
    Loads DAG documentation from workflow.md file.

    Returns:
        String containing the markdown documentation
    """
    dag_file = Path(__file__)
    workflow_md_path = dag_file.parent / "workflow.md"

    with open(workflow_md_path) as f:
        return f.read()


def load_config(wop_stage: str) -> dict:
    """
    Loads contents of specified YAML files in the config directory into a dict.

    Args:
        wop_stage: Deployment environment (e.g., 'dev', 'prod')

    Returns:
        Dictionary of configuration parameters
    """
    import yaml

    dag_file = Path(__file__)
    file_yaml = f"config/{wop_stage}.yaml"

    with open(dag_file.parent / file_yaml) as f:
        return yaml.safe_load(f)
