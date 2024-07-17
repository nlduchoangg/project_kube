import requests

# Replace with your Airflow base URL
AIRFLOW_BASE_URL = 'http://localhost:8080/api/v1/dags'

# Replace with your authentication details if needed
auth = ('airflow', 'airflow')  # Use None if no authentication
list_task_id = {'read_file', 'print_hello', 'print_goodbye'}

def get_dags(base_url, auth=None):
    response = requests.get(base_url, auth=auth)
    if response.status_code == 200:
        return response.json()['dags']
    else:
        raise Exception(f"Failed to get DAGs: {response.status_code} - {response.text}")

def get_tasks_list_from_dag_id(base_url, dag_id, auth=None):
    url = f"{base_url}/{dag_id}/tasks"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        tasks = response.json()['tasks']
        return [task['task_id'] for task in tasks]
    else:
        raise Exception(f"Failed to get tasks for DAG {dag_id}: {response.status_code} - {response.text}")

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

# tới đoạn này ở phần cuối của url có số 1 đó chính là vị trí của file log ghi lại số lần retries dag của airflow thế nên cần
# phải cập nhật lấy ra số lần retries và dùng vòng lặp nhét nó vào đoạn cuối của url.
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
        #print(status)
        task_list = get_tasks_list_from_dag_id(AIRFLOW_BASE_URL, 'read_file', auth)
        if status[0]['state'] == 'failed':
            for task_id in task_list:
                logs = get_task_logs(AIRFLOW_BASE_URL, 'read_file', status[0]['dag_run_id'], task_id, auth)
                print('================================================ LOG OF TASK NAME IS: {} ================================================'.format(task_id))
                print(logs)

        # elif status[0]['state'] == 'failed':
        #     for task_id in task_list:
        #         logs = get_task_logs(AIRFLOW_BASE_URL, 'read_file', status[0]['dag_run_id'], task_id, auth)
        #         print('================================================ LOG OF TASK NAME IS: {} ================================================'.format(task_id))
        #         print(logs)
        else:
            print("Unknow state")


        #print(f"DAG ID: {'read_file'}, Latest Status: {status}")
    except Exception as e:
        print(e)
