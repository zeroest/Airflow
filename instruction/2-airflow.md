
# [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html)

## Why Apache Airflow?

- Workflow as Code: Define workflows as code using Python.
  - Python을 사용하여 워크플로우를 코드로 정의
- Scalability: Supports parallel and distributed execution of tasks.
  - 병렬 및 분산 실행을 지원하여 작업(task)의 성능을 최적화
- Dependency Management: Manages dependencies between tasks, ensuring that tasks are executed in the correct order and that upstream tasks complete successfully before downstream tasks start.
  - 작업 간 의존성을 관리하여 올바른 순서로 실행되도록 보장
  - 상위 작업이 완료된 후 하위 작업이 실행되도록 조정
- Monitoring and Alerting: Provides a web-based user interface, logs, and alerts.
  - 웹 기반 인터페이스, 로그, 알림 기능을 제공하여 워크플로우 상태를 쉽게 모니터링
- Extensibility and Integrations: Offers a wide range of built-in operators and sensors for common tasks, such as executing SQL queries, running Python scripts, interacting with APIs, and more.
  - SQL 쿼리 실행, Python 스크립트 실행, API 연동 등 다양한 작업을 수행할 수 있는 내장 연산자(operators) 및 센서(sensors)를 제공
- Ecosystem and Community: Has a vibrant and active community of users and contributors, resulting in a rich ecosystem of plugins, extensions, and integrations.
  - 활발한 사용자 및 기여자 커뮤니티가 존재하며, 플러그인, 확장 기능, 다양한 통합 옵션을 갖춘 풍부한 에코시스템을 제공
- DAG Visualization: Provides a graphical representation of your workflows, allowing you to visualize the structure and dependencies of your data pipelines.
  - 그래픽 인터페이스를 통해 워크플로우를 시각적으로 표현하여 데이터 파이프라인의 구조와 작업 간 의존성을 쉽게 확인할 수 있도록 지원
- Fault Tolerance and Retries: Offers built-in mechanisms for handling task failures and retries. You can configure retry policies, set task timeouts, and define error handling strategies.
  - 작업 실패와 재시도를 처리하는 기본 메커니즘을 제공
  - 사용자는 재시도 정책을 설정하고, 작업 시간 초과(timeouts)를 지정하며, 오류 처리 전략을 정의

## Key Components

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

