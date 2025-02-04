  
# Key Components

![Airflow all flow](./img/airflow-all-flow.gif)
https://learnwithaakash.com/2023/06/26/a-beginner-guide-to-airflow-components/

- Web Server: A user interface that allows users to monitor, manage, and visualize the status and progress of their workflows.
  - 사용자 인터페이스(UI)를 제공하여 워크플로우의 상태와 진행 상황을 모니터링, 관리 및 시각화할 수 있도록 지원
- Scheduler: It orchestrates the execution of tasks based on their dependencies and schedules defined in the DAGs (When & Where).
  - DAG에서 정의된 작업의 실행을 의존성과 스케줄(언제 & 어디서 실행할지)에 따라 오케스트레이션
- Metadata Database: Airflow uses a database to store metadata about DAGs, tasks, and their state, providing persistence and fault tolerance.
  - Airflow는 DAG, 작업(Task) 및 상태(State)에 대한 메타데이터를 저장하는 데이터베이스를 사용 
  - 데이터의 지속성(Persistence)과 장애 허용성(Fault Tolerance)을 제공
- Executor: It determines how tasks are executed. Airflow supports various executors, such as LocalExecutor, CeleryExecutor, and KubernetesExecutor, which allow for parallel and distributed task execution.
  - 작업이 실행되는 방식을 결정
  - LocalExecutor, CeleryExecutor, KubernetesExecutor 등 다양한 실행기를 지원하여 병렬 및 분산 작업 실행이 가능
- Worker: The process that executes tasks, as defined by the executor.
  - 실행기(Executor)에 의해 정의된 작업을 실제로 실행하는 프로세스
- Triggerer: A separate process that supports deferrable operators.
  - 지연 실행이 가능한 연산자(Deferrable Operators)를 지원하는 별도의 프로세스

cf. [Architecture Overview](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html#)

## [DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)

DAG (Directed Acyclic Graph) is a fundamental concept used to define and represent workflows or data pipelines. A DAG is a collection of tasks with dependencies between them, forming a directed graph structure where the nodes represent tasks and the edges represent the dependencies.
- 워크플로우 또는 데이터 파이프라인을 정의하고 표현하는 데 사용되는 기본 개념
- DAG는 서로 의존성을 가진 작업들의 집합으로, 노드는 작업을 나타내고 간선은 의존성을 나타내는 방향 그래프 구조를 형성

Each task within a DAG represents a unit of work or a computational step to be executed. Tasks can be written in any programming language or script, such as Python, Bash, or SQL. Examples of tasks can include extracting data from a source, transforming data, loading data into a destination, or running a machine learning model.
- DAG 내의 각 태스크는 실행해야 할 작업 단위 또는 계산 단계로 구성
- 태스크는 Python, Bash, SQL과 같은 다양한 프로그래밍 언어 또는 스크립트로 작성
- 데이터 원본에서 데이터를 추출하거나, 데이터를 변환하거나, 대상에 데이터를 적재하거나, 머신 러닝 모델을 실행하는 작업 등이 포함될 수 있음

Airflow uses Python scripts to define and configure DAGs. In the DAG definition script, you define tasks, their dependencies, and any other properties or parameters. The DAG script also specifies the schedule on which the DAG should be triggered, such as a specific time or a cron expression.
- Airflow는 Python 스크립트를 사용하여 DAG를 정의하고 구성
- DAG 정의 스크립트에서는 태스크, 그들의 의존성, 그리고 기타 속성이나 매개변수를 정의
- 또한 DAG 스크립트에서는 특정 시간이나 cron 표현식과 같은 스케줄을 지정하여 DAG가 실행될 시점을 설정

## [Tasks](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#)

A Task is the basic unit of execution in Airflow. Tasks are arranged into DAGs and then have upstream and downstream dependencies set between them in order to express the order they should run in.
- 태스크는 Airflow에서 실행의 기본 단위
- 태스크는 DAG 내에 배치되며, 실행 순서를 나타내기 위해 상위(Upstream) 및 하위(Downstream) 의존성이 설정

Task Instance  
Much in the same way that a DAG is instantiated into a DAG Run each time it runs, the tasks under a DAG are instantiated into Task Instances.
  - DAG가 실행될 때마다 DAG Run으로 인스턴스화되는 것과 마찬가지로, DAG 내의 태스크들도 각각 태스크 인스턴스로 인스턴스화


## [Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html#)

These are pre-defined or custom-defined components that define the individual tasks within a workflow. Airflow provides a rich set of built-in operators for various purposes, such as PythonOperator, BashOperator, and more.
- 이들은 워크플로우 내에서 개별 태스크를 정의하는 사전 정의된 또는 사용자 정의된 구성 요소
- Airflow는 다양한 용도를 위한 풍부한 내장 연산자(Operator) 세트를 제공하며, 예로는 PythonOperator, BashOperator 등이 있음

오퍼레이터 예제 
- Action Operator
  - BashOperator
  - PythonOperator
- Transfer Operator
  - S3FileTransferOperator
- Sensor Operator
  - FileSensor
  - TimeSensor
  - HdfsSensor

