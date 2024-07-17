from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Định nghĩa hàm để đọc và hiển thị nội dung file .txt
def read_file():
    file_paths = [
        '/opt/airflow/dags/data/data_test.txt',
        '/opt/airflow/dags/data/produc.txt'
        # '/home/hoang/project_kub/airflow-docker/data/data_test.txt',
        # '/home/hoang/project_kub/airflow-docker/data/product.txt'
    ]
    for filepath in file_paths:
        with open(filepath, 'r') as file:
            content = file.read()
            print(content)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}
def hello_world():
    print("Hello World!")

def goodbye_world():
    print("Good Bye!")

# Khởi tạo DAG
dag = DAG(
    dag_id='read_file',
    default_args=default_args,
    description='DAG to read and display content of data_test.txt file',
    schedule='@once',
)

# Định nghĩa task để gọi hàm read_file
read_file_task = PythonOperator(
    task_id='read_file_task',
    python_callable=read_file,
    dag=dag,
)

print_hello = PythonOperator(
    task_id='print_hello',
    python_callable=hello_world,
    dag=dag,
)

print_goodbye = PythonOperator(
    task_id='print_goodbye',
    python_callable=goodbye_world,
    dag=dag,
)

# Định nghĩa trình tự thực hiện các task
read_file_task >> print_hello >> print_goodbye


# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
#
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 7, 12),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }
#
# dag = DAG(
#     'kubernetes_operator_example',
#     default_args=default_args,
#     description='Run KubernetesPodOperator with custom image',
#     schedule=timedelta(days=1),  # or your preferred schedule
# )
#
# # task = KubernetesPodOperator(namespace='default',
# #                                 image="localhost:5000/images_test:latest",
# #                                 cmds=["python3","-c"],
# #                                 arguments=["print('hello world')"],
# #                                 labels={"foo": "bar"},
# #                                 name="passing-test",
# #                                 task_id="passing-task",
# #                                 get_logs=True,
# #                                 dag=dag
# #                                 )
#
# #đang bí đoạn tại sao các container trên pod ko hiển thị log đã chạy từ file h.py
# task = KubernetesPodOperator(
#     task_id='kubernetes_task',
#     name='kubernetes_task',
#     namespace='default',  # or your preferred namespace
#     image='localhost:5000/images_test:latest',
#     cmds=['python3'],
#     arguments=['/home/hoang/project_kub/airflow-docker/scripts/h.py'],
#     dag=dag,
# )
#
#
# task

