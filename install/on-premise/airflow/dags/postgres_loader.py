# Define the DAG
with DAG(
    'postgres_loader',
    description='PostgreSQL Loader Example',
    default_args=default_args,
    schedule_interval='0 0 * * *',
    catchup=False
) as dag:
    
    # Task: Execute a SQL query using PostgresOperator
    sql_query = """
    INSERT INTO sample_table (key, value)
    VALUES ('hello', 'world')
    """

    postgres_task = PostgresOperator(
        task_id='execute_sql_query',
        postgres_conn_id='my_postgres_connection',
        sql=sql_query,
        dag=dag
    )

