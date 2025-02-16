
# [Install]()

## virutualenv

```bash
python3 -m pip install virtualenv

# Defaulting to user installation because normal site-packages is not writeable
# Collecting virtualenv
#   Downloading virtualenv-20.29.2-py3-none-any.whl.metadata (4.5 kB)
# Requirement already satisfied: distlib<1,>=0.3.7 in /Users/zero/Library/Python/3.9/lib/python/site-packages (from virtualenv) (0.3.9)
# Requirement already satisfied: filelock<4,>=3.12.2 in /Users/zero/Library/Python/3.9/lib/python/site-packages (from virtualenv) (3.17.0)
# Requirement already satisfied: platformdirs<5,>=3.9.1 in /Users/zero/Library/Python/3.9/lib/python/site-packages (from virtualenv) (4.3.6)
# Downloading virtualenv-20.29.2-py3-none-any.whl (4.3 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 11.0 MB/s eta 0:00:00
# Installing collected packages: virtualenv
#   WARNING: The script virtualenv is installed in '/Users/zero/Library/Python/3.9/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed virtualenv-20.29.2

python3 -m virtualenv venv

# created virtual environment CPython3.9.6.final.0-64 in 137ms
#   creator CPython3macOsFramework(dest=/Users/zero/Program/airflow/local-standalone/venv, clear=False, no_vcs_ignore=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/zero/Library/Application Support/virtualenv)
#     added seed packages: pip==25.0.1, setuptools==75.8.0, wheel==0.45.1
#   activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

```

```bash
source venv/bin/activate

pip install -r requirements.txt

deactivate
```

## [Quick Start - Standalone](https://airflow.apache.org/docs/apache-airflow/stable/start.html)


1. Set Airflow Home (optional):

Airflow requires a home directory, and uses ~/airflow by default, but you can set a different location if you prefer.   
The AIRFLOW_HOME environment variable is used to inform Airflow of the desired location.  
This step of setting the environment variable should be done before installing Airflow so that the installation process knows where to store the necessary files.

```bash
export AIRFLOW_HOME=~/airflow
```

2. Install Airflow using the constraints file, which is determined based on the URL we pass:

```bash
AIRFLOW_VERSION=2.10.5

# Extract the version of Python you have installed. 
# If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.10.5 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.8.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

```bash
airflow standalone

# webserver  | [2025-02-16 23:31:50 +0900] [55111] [INFO] Starting gunicorn 23.0.0
# webserver  | [2025-02-16 23:31:50 +0900] [55111] [INFO] Listening at: http://0.0.0.0:8080 (55111)
# webserver  | [2025-02-16 23:31:50 +0900] [55111] [INFO] Using worker: sync
# webserver  | [2025-02-16 23:31:50 +0900] [55131] [INFO] Booting worker with pid: 55131
# webserver  | [2025-02-16 23:31:50 +0900] [55132] [INFO] Booting worker with pid: 55132
# webserver  | [2025-02-16 23:31:50 +0900] [55133] [INFO] Booting worker with pid: 55133
# webserver  | [2025-02-16 23:31:50 +0900] [55134] [INFO] Booting worker with pid: 55134
# standalone | Airflow is ready
# standalone | Login with username: admin  password: E3aT94ey5zSsSyGH
# standalone | Airflow Standalone is for development purposes only. Do not use this in production!
```

```
http://0.0.0.0:8080
id: admin
pw: E3aT94ey5zSsSyGH
```

Disable examples 
```bash
vim $AIRFLOW_HOME/airflow.cfg

load_examples = False
```


## [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.5/docker-compose.yaml'
```

```
http://0.0.0.0:8080
id: airflow
pw: airflow
```



