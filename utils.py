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
    config_dir = dag_file.parent / "config"

    # Define possible filenames for each stage
    stage_mapping = {
        "dev": ["dev.yaml", "development.yaml"],
        "prod": ["prod.yaml", "production.yaml"],
    }

    # Get list of files to check, defaulting to just the stage name
    files_to_check = stage_mapping.get(wop_stage, [f"{wop_stage}.yaml"])

    for filename in files_to_check:
        file_path = config_dir / filename
        if file_path.exists():
            with open(file_path) as f:
                return yaml.safe_load(f)

    # If no file found, raise error
    raise FileNotFoundError(
        f"Could not find configuration file for stage '{wop_stage}'. "
        f"Checked: {', '.join(files_to_check)}"
    )
