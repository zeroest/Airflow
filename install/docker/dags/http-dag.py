import json
from airflow import DAG
# from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.http.sensors.http import HttpSensor
# from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.python_operator import PythonOperator
# https://airflow.apache.org/docs/apache-airflow-providers-postgres/stable/_api/airflow/providers/postgres/hooks/postgres/index.html
from airflow.providers.postgres.hooks.postgres import PostgresHook
from pandas import json_normalize
from datetime import datetime

def _extract_data(**context):
    response = context['ti'].xcom_pull(task_ids='get_op')
    starwars_character = json_normalize({
        "name": response['name'],
        "height": response["height"],
        "mass": response["mass"]
    })
    starwars_character.to_csv("/tmp/starwars_character.csv", header=False, index=None)

def _store_character(**context):
    hook = PostgresHook(
        postgres_conn_id='my_postgres_connection'
    )
    # Executes SQL using psycopg2 copy_expert method. Necessary to execute COPY command without access to a superuser.
    hook.copy_expert(
        filename="/tmp/starwars_character.csv",
        sql="COPY starwars_character FROM stdin WITH DELIMITER as ','"
    )

# Define the DAG
with DAG('http_dag',
         description='http dag',
         schedule_interval='0 0 * * *',
         start_date=datetime(2023, 7, 1),
         catchup=False) as dag:

    # task_create_table_op = PostgresOperator(
    #     task_id="create_table_op",
    #     postgres_conn_id='my_postgres_connection',
    #     sql='''
    #         CREATE TABLE IF NOT EXISTS starwars_character (
    #             name TEXT NOT NULL,
    #             height TEXT NOT NULL,
    #             mass TEXT NOT NULL
    #         );
    #     '''
    # )
    task_create_table_op = SQLExecuteQueryOperator(
        task_id="create_table_op",
        conn_id='my_postgres_connection',
        sql='''
            CREATE TABLE IF NOT EXISTS starwars_character (
                name TEXT NOT NULL,
                height TEXT NOT NULL,
                mass TEXT NOT NULL
            );
        '''
    )

    # task_get_op = SimpleHttpOperator(
    #     task_id="get_op",
    #     http_conn_id="my_http_connection",
    #     endpoint="/api/people/1/",
    #     headers={"Content-Type": "application/json"},
    #     method='GET',
    #     response_filter=lambda response: json.loads(response.text),
    #     log_response=True
    # )
    task_get_op = HttpOperator(
        task_id="get_op",
        http_conn_id="my_http_connection",
        endpoint="/api/people/1/",
        headers={"Content-Type": "application/json"},
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    task_extract_data_op = PythonOperator(
        task_id="extract_data_op",
        python_callable=_extract_data,
        provide_context=True
    )

    task_store_op = PythonOperator(
        task_id="store_op",
        python_callable=_store_character
    )

task_create_table_op >> task_get_op >> task_extract_data_op >> task_store_op
