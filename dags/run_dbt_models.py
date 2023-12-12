from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

args = {
    'owner': 'Ezgi Karvan',
    'start_date': days_ago(1),
    'depends_on_past': False,
}

dag = DAG(
    dag_id = 'run_dbt_models',
    default_args = args,
    schedule_interval = None
)

with dag:
    
    run_dbt_models = BashOperator(
    task_id = 'run_dbt_models',
    bash_command = 'cd /dbt && dbt run --profiles-dir .',
    dag = dag
    )

