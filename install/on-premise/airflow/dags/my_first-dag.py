from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("What's up Airflow!")

# Define the DAG
with DAG('sample_dag',
         description='A simple DAG',
         schedule_interval='0 0 * * *', # crontab syntax
         start_date=datetime(2025, 2, 16),
         catchup=False) as dag:

    # Task 1: Print hello
    task1 = PythonOperator(task_id='print_hello_task',
                           python_callable=print_hello,
                           dag=dag)

    # Task 2: Dummy task
    task2 = DummyOperator(task_id='dummy_task',
                          dag=dag)

# Define the task dependencies
task1 >> task2

