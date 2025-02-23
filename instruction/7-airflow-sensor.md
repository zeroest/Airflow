
# Sensor

In Apache Airflow, a sensor is a type of operator that pauses the execution of a task within a DAG (Directed Acyclic Graph) until a specific condition is met.   
- Apache Airflow에서 센서는 특정 조건이 충족될 때까지 DAG(Directed Acyclic Graph) 내의 태스크 실행을 일시 중지하는 연산자 유형

Sensors are used to wait for external events, changes in the system, or certain conditions to be satisfied before proceeding with the execution of downstream tasks.
- 센서는 외부 이벤트, 시스템 변경 또는 특정 조건이 충족될 때까지 대기한 후, 다운스트림 태스크의 실행을 진행하도록 사용

Type of sensor
- FileSensor: Waits for a file or directory to become available.
- TimeSensor: Pauses until a specific time or schedule is reached.
- ExternalTaskSensor: Waits for the completion of a specific task in another DAG.
- HttpSensor: Waits for an HTTP endpoint to return a specific response.
- SqlSensor: Waits for a specific condition to be met in a SQL query result.
- HdfsSensor: Waits for a file or directory to be available in HDFS (Hadoop Distributed File System).
- S3KeySensor: Waits for an S3 key (file) to be available in AWS S3.

mode
- poke: Continuously executes the condition check until the condition is met.
  - 조건이 충족될 때까지 지속적으로 상태를 확인
- reschedule (default): Reschedules itself to run again based on the poke_interval parameter when the condition is not met.
  - 조건이 충족되지 않으면 poke_interval 매개변수에 따라 다시 실행되도록 예약
  - poke_interval: Defines how frequently the sensor checks for the condition.
    - 센서가 조건을 확인하는 빈도를 정의

```python
from airflow.sensors.sql import SqlSensor

sal_sensor = SqlSensor(
    task_id='wait_for_condition',
    conn_id='my_postgres_connection',
    sql="SELECT COUNT(*) FROM sample_table WHERE key='hello'",
    mode='poke',
    poke_interval=30,
    dag=dag
)
```

cf. https://heumsi.github.io/apache-airflow-tutorials-for-beginner/dags/07-providers/#provider-package-%E1%84%86%E1%85%A9%E1%86%A8%E1%84%85%E1%85%A9%E1%86%A8

## Example

[sql_sensor.py](../install/on-premise/airflow/dags/sql_sensor.py)
