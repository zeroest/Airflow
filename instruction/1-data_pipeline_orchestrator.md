
# Data Pipeline Orchestrator

- A data pipeline orchestrator is a tool or platform that manages and coordinates the execution of data pipelines.
  - 데이터 파이프라인의 실행을 관리하고 조정하는 도구 또는 플랫폼
- It provides a framework to define, schedule, and monitor the flow of data and tasks within a pipeline.
  - 데이터 및 작업의 흐름을 정의하고, 스케줄링하며, 모니터링할 수 있는 프레임워크를 제공
- The orchestrator ensures that data flows smoothly between different stages or components of the pipeline, coordinating the dependencies and execution order of tasks.
  - 파이프라인의 다양한 단계 또는 구성 요소 간의 데이터 흐름이 원활하게 이루어지도록 보장하며, 작업 간의 의존성과 실행 순서를 조정

## Main Functions of a Data Pipeline Orchestrator

- Workflow Definition: It allows users to define the structure and logic of the data pipeline, specifying the sequence of tasks, their dependencies, and the data transformations to be applied.
  - 데이터 파이프라인의 구조와 논리를 정의할 수 있도록 지원
  - 작업(task)의 순서, 의존성, 적용할 데이터 변환 등을 지정
- Task Scheduling: The orchestrator schedules the execution of tasks based on their dependencies and predefined schedules. It ensures that tasks are executed in the correct order and that dependencies are met.
  - 오케스트레이터는 작업 간의 의존성과 사전 정의된 일정에 따라 작업 실행을 스케줄링
  - 작업이 올바른 순서로 실행되도록 보장하며, 필요한 의존성이 충족되었는지 확인
- Dependency Management: The orchestrator handles the dependencies between tasks, ensuring that a task is not executed until its upstream dependencies are successfully completed. This ensures the integrity and consistency of the data flow.
  - 오케스트레이터는 작업 간 의존성을 관리하여, 상위 작업이 성공적으로 완료될 때까지 하위 작업이 실행되지 않도록 함 
  - 이를 통해 데이터 흐름의 무결성과 일관성을 보장
- Data Movement: The orchestrator manages the movement of data between different stages or components of the pipeline. It coordinates the transfer of data from source systems, through intermediate processing steps, to destination systems or storage.
  - 오케스트레이터는 데이터가 파이프라인의 다양한 단계 또는 구성 요소 간에 이동하는 과정을 관리
  - 원본 시스템에서 데이터를 추출하여 중간 처리 단계를 거친 후, 최종 목적지 시스템이나 저장소로 전송하는 과정을 조정
- Monitoring and Error Handling: The orchestrator provides visibility into the execution of the data pipeline, allowing users to monitor the progress, status, and performance of tasks. It also handles error handling and retries in case of failures, ensuring fault tolerance and data integrity.
  - 오케스트레이터는 데이터 파이프라인 실행 상태를 모니터링할 수 있도록 가시성을 제공
  - 사용자는 작업의 진행 상태, 실행 결과 및 성능을 확인할 수 있으며, 오류가 발생할 경우 자동으로 재시도(retry)하거나 오류를 처리하여 장애 허용성(fault tolerance)과 데이터 무결성(data integrity)을 보장
- Scalability and Parallel Execution: Some orchestrators support parallel execution of tasks, allowing multiple tasks to run concurrently to improve pipeline performance. They can scale horizontally to handle large volumes of data and distributed processing.
  - 일부 오케스트레이터는 작업의 병렬 실행을 지원하여 여러 작업을 동시에 수행함으로써 파이프라인 성능을 향상 
  - 또한 수평적 확장(horizontal scaling)이 가능하여 대량의 데이터 처리 및 분산 처리를 효율적으로 수행

## 데이터 파이프라인 오케스트레이터 예시

- [Airflow](https://airflow.apache.org/)
- [oozie](https://oozie.apache.org/)
- [luigi](https://github.com/spotify/luigi)
- [AWS Step Functions](https://aws.amazon.com/ko/step-functions/)
- [Temporal](https://temporal.io/)



