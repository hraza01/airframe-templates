"""
Task definitions for Airflow DAG.

This module contains reusable task functions using the TaskFlow API.
All tasks are decorated with @task and can be imported into DAG definitions.
"""

from airflow.decorators import task


@task
def call_external_api(api_url: str) -> dict:
    """
    Example Python task that makes an API call.
    The return value is automatically stored in XCom for downstream tasks.

    Args:
        api_url: The API endpoint to call

    Returns:
        Dictionary with API response data (automatically pushed to XCom)
    """
    import requests

    # Make API call
    print(f"Calling API: {api_url}")
    response = requests.get(api_url, timeout=30)

    # Extract response data
    status_code = response.status_code

    # Check if successful
    if status_code == 200:
        response_data = response.json()
        result = {
            "status_code": status_code,
            "status": "success",
            "message": "API call successful",
            "data": response_data,
        }
    else:
        result = {
            "status_code": status_code,
            "status": "error",
            "message": f"API call failed with status {status_code}",
            "data": None,
        }

    print(f"API Response - Status: {status_code}, Message: {result['message']}")

    # Return value is automatically pushed to XCom by TaskFlow API
    return result


def validate_api_response(**context) -> bool:
    """
    Checks if API call was successful (status_code == 200).
    Returns True to continue, False to skip downstream tasks.
    This uses ShortCircuitOperator pattern.

    Args:
        **context: Airflow context containing task instance

    Returns:
        True if API call was successful, False otherwise
    """
    ti = context["ti"]
    api_response = ti.xcom_pull(task_ids="call_external_api")

    status_code = api_response.get("status_code")

    if status_code == 200:
        print(f"✅ API call successful with status {status_code}.")
        return True
    else:
        print(f"❌ API call failed with status {status_code}.")
        return False
