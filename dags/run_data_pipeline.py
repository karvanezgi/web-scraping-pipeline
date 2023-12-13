from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

args = {
    'owner': 'Ezgi Karvan',
    'start_date': days_ago(1)
}

dag = DAG(
    dag_id = 'run_data_pipeline',
    default_args = args,
    schedule_interval = '@daily',
    catchup=False,
)

with dag:
    
    load_data_to_raw_zone = TriggerDagRunOperator(
        task_id = "load_data_to_raw_zone",
        trigger_dag_id = "load_data_to_raw_zone",
        wait_for_completion = True
    )
    
    
    run_dbt_models = TriggerDagRunOperator(
        task_id = "run_dbt_models",
        trigger_dag_id = "run_dbt_models",
        wait_for_completion = True
    )

    
load_data_to_raw_zone >> run_dbt_models