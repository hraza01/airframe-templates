import os
from pathlib import Path

import pendulum
from airflow import DAG
from airflow.operators.python import ShortCircuitOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

# fmt: off
# isort: off
from __PROJECT_NAME__.tasks import call_external_api, validate_api_response
from __PROJECT_NAME__.utils import load_config, load_workflow_md
# isort: on
# fmt: on


def main():
    wop_stage = os.environ["WOP_STAGE"]
    params = load_config(wop_stage)
    doc_md = load_workflow_md()

    dag_args = {
        # DAG
        "dag_id": Path(__file__).parent.name,
        # "schedule_interval": "0 0 * * 1",  # Every Monday at 00:00
        "schedule_interval": None,  # Manually triggered
        "doc_md": doc_md,
        "max_active_runs": 1,
        "dagrun_timeout": pendulum.duration(minutes=59),
        "template_searchpath": [f"{Path(__file__).parents[0]}"],
        "params": dict(params),
        "catchup": False,
        "is_paused_upon_creation": True,
        "render_template_as_native_obj": True,
        "default_args": {
            "start_date": pendulum.datetime(2025, 6, 12, tz="UTC"),
            "owner": "__DAG_AUTHOR__",
            "email": params["email_recipients"],
            "depends_on_past": False,
            "retries": 2,
            "retry_delay": pendulum.duration(minutes=1),
            "email_on_failure": False,
            "email_on_retry": False,
        },
    }

    create_dag(dag_args)


def create_dag(dag_args):
    with DAG(**dag_args) as dag:
        """
        No logic outside of tasks(operators) or they are constantly run by scheduler
        """

        # Trigger external API call (Airflow orchestrates, doesn't process)
        python_task = call_external_api("https://jsonplaceholder.typicode.com/posts/1")

        # Create validation task with short-circuit behavior
        validate_task = ShortCircuitOperator(
            task_id="validate_api_response",
            python_callable=validate_api_response,
        )

        sql_task = BigQueryInsertJobOperator(
            task_id="sql_task",
            configuration={
                "query": {
                    "query": "{% include '/sql/example.sql' %}",
                    "useLegacySql": False,
                }
            },
        )

        templated_sql_task = BigQueryInsertJobOperator(
            task_id="templated_sql_task",
            configuration={
                "query": {
                    "query": "{% include '/sql/template.sql' %}",
                    "useLegacySql": False,
                }
            },
            # Pass upstream task ID to allow SQL template to pull XCom data
            params={"upstream_task_id": "call_external_api"},
        )

        # Set task dependencies
        # Only execute templated_sql_task if API call was successful (200)
        python_task >> sql_task
        python_task >> validate_task >> templated_sql_task

    globals()[dag.dag_id] = dag


main()
