import requests
from requests.auth import HTTPBasicAuth

headers = {
    'Accept': 'text/plain',
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'session=4a8c4af9-581d-4afa-ab80-c484693dd160.RjzPGdeK_ogI6I_M7FCVw8B6vEU',
    'Referer': 'http://localhost:8080/dags/read_file/grid?dag_run_id=manual__2024-07-16T07%3A58%3A12.449677%2B00%3A00&tab=logs&task_id=read_file_task',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'full_content': 'false',
}

auth = HTTPBasicAuth('airflow', 'airflow')

response = requests.get(
    'http://localhost:8080/api/v1/dags/read_file/dagRuns/manual__2024-07-16T07:58:12.449677+00:00/taskInstances/read_file_task/logs/1',
    params=params,
    auth=auth,
    headers=headers,
)

print(response.text)
