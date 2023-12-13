from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
    
args = {
    'owner': 'Ezgi Karvan',
    'start_date': days_ago(1)
}

dag = DAG(
    dag_id = 'create_tables',
    default_args = args,
    schedule_interval = '@once', # make this workflow happen every day
    catchup = False,
)

with dag:
    
    create_raw_zone_table = PostgresOperator(
        task_id = 'create_raw_zone_table',
        postgres_conn_id = "postgres_default",
        sql = """
            create table if not exists restaurants(
            id serial, name VARCHAR (250)  NOT NULL, category VARCHAR (250), price_range integer, rating VARCHAR (10)
            )
        """,
    )
    
    create_raw_zone_dbt_table = PostgresOperator(
        task_id = 'create_raw_zone_dbt_table',
        postgres_conn_id = "postgres_default",
        sql = """
            create table if not exists stg_restaurants(
            id serial, name VARCHAR (250)  NOT NULL, category VARCHAR (250), price_range integer, rating VARCHAR (10)
            )
        """,
    )
    
    create_dbt_core_table = PostgresOperator(
        task_id = 'create_dbt_core_table',
        postgres_conn_id = "postgres_default",
        sql = """
            CREATE TABLE if not exists core_restaurants(
            id serial, name VARCHAR (250) NOT NULL, category VARCHAR (250), price_range integer, rating VARCHAR (10), ingestion_date date
            )
        """,
    )    
    create_dbt_report_tables = PostgresOperator(
        task_id = 'create_dbt_report_tables',
        postgres_conn_id = "postgres_default",
        sql = """
            CREATE TABLE if not exists ratings_per_cousine(
            id serial,rating VARCHAR (10), category VARCHAR (250), count integer
            );
            CREATE TABLE if not exists cousines_per_price_range(
            id serial, category VARCHAR (250), price_range integer, count integer
            );
            CREATE TABLE if not exists cousines_per_ingestion_date(
            id serial, category VARCHAR (250), ingestion_date date, count integer
            );
        """,    
    )