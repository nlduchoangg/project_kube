import requests

# Replace with your Airflow base URL
AIRFLOW_BASE_URL = 'http://localhost:8080/api/v1/dags'

# Replace with your authentication details if needed
auth = ('airflow', 'airflow')  # Use None if no authentication



def get_dags(base_url, auth=None):
    response = requests.get(base_url, auth=auth)
    if response.status_code == 200:
        return response.json()['dags']
    else:
        raise Exception(f"Failed to get DAGs: {response.status_code} - {response.text}")

def get_latest_dag_run_status(base_url, dag_id, auth=None):
    url = f"{base_url}/{dag_id}/dagRuns?order_by=-start_date&limit=1"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        runs = response.json()['dag_runs']
        if runs:
            return runs
        else:
            return 'No runs found'
    else:
        raise Exception(f"Failed to get DAG run status for {dag_id}: {response.status_code} - {response.text}")

def get_task_logs(base_url, dag_id, dag_run_id, task_id, auth=None):
    url = f"{base_url}/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/1"
    #print(url)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to get task logs: {response.status_code} - {response.text}")

if __name__ == "__main__":
    try:
        dags = get_dags(AIRFLOW_BASE_URL, auth)
        print("Latest status of each DAG:")
        status = get_latest_dag_run_status(AIRFLOW_BASE_URL, 'read_file', auth)

        #print log of task with dag_id, dag_run_id, task_id param
        logs = get_task_logs(AIRFLOW_BASE_URL, 'read_file', status[0]['dag_run_id'], 'read_file_task', auth)
        #print(type(logs))
        print(logs)

        #print(f"DAG ID: {'read_file'}, Latest Status: {status}")
    except Exception as e:
        print(e)
