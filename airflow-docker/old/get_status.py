# import requests
# from requests.auth import HTTPBasicAuth
#
# # Thay đổi các giá trị này cho phù hợp với môi trường của bạn
# airflow_host = 'http://localhost:8080'  # Địa chỉ host của Airflow webserver
# dag_id = 'read_file'  # ID của DAG
# task_id = 'read_file_task'  # ID của task
#
# # ID của DAG Run và task log cần lấy thông tin
# dag_run_id = 'manual__2024-07-16T07:58:12.449677+00:00'  # ID của DAG Run
# task_log_id = '460d3c63a04e'  # ID của task log
#
# # Endpoint để lấy log của một task trong một DAG
# endpoint = f'{airflow_host}/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_log_id}'
# print(endpoint)
# # Thông tin xác thực
# username = "airflow"
# password = "airflow"
#
# # Xác thực và gửi HTTP GET request đến Airflow API
# response = requests.get(endpoint, auth=HTTPBasicAuth(username, password))
#
# # Kiểm tra phản hồi từ Airflow API
# if response.status_code == 200:
#     task_logs = response.json().get('logs')
#     print(f"Log của task {task_id} trong DAG {dag_id}:")
#     print(task_logs)
# else:
#     print(f"Lỗi khi lấy log của task {task_id}: {response.text}")
#
#

import requests
from requests.auth import HTTPBasicAuth

# Thông tin đăng nhập
username = 'airflow'
password = 'airflow'
base_url = 'http://host.docker.internal:8080/api/v1'  # Thay đổi thành URL của Airflow API của bạn

# Tạo session và đăng nhập
session = requests.Session()
session.auth = HTTPBasicAuth(username, password)

try:
    # Gửi yêu cầu GET để lấy thông tin user từ API của Airflow
    response = session.get(f"{base_url}/users/{username}")
    response.raise_for_status()  # Nếu có lỗi, ném ra một exception

    # Nếu không có lỗi, đăng nhập thành công
    print(f"Đăng nhập Airflow thành công với user '{username}'")
except requests.exceptions.RequestException as e:
    print(f"Lỗi khi gửi yêu cầu: {e}")

# Lấy log của task từ DAG
dag_id = 'read_file'
task_id = 'read_file_task'

try:
    # Gửi yêu cầu GET để lấy logs của task từ DAG
    response = session.get(f"{base_url}/dags/{dag_id}/dagRuns/latest/taskInstances/{task_id}/logs")
    response.raise_for_status()  # Nếu có lỗi, ném ra một exception
    logs = response.json()['content']
    print(f"Logs của task '{task_id}' trong DAG '{dag_id}':")
    print(logs)
except requests.exceptions.RequestException as e:
    print(f"Lỗi khi gửi yêu cầu: {e}")
except KeyError as e:
    print(f"Lỗi khi xử lý logs: {e}")




