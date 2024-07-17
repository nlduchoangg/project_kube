import requests

# Replace with your Airflow base URL
AIRFLOW_BASE_URL = 'http://localhost:8080/api/v1/dags'

# Replace with your authentication details if needed
auth = ('airflow', 'airflow')  # Use None if no authentication

def get_dags(base_url, auth=None):
    response = requests.get(base_url, auth=auth)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get DAGs: {response.status_code} - {response.text}")

if __name__ == "__main__":
    try:
        dags = get_dags(AIRFLOW_BASE_URL, auth)
        print("List of DAGs:")
        for dag in dags['dags']:
            print(dag['dag_id'])
    except Exception as e:
        print(e)
