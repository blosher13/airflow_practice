from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG('user_processing', start_date = datetime(2025,1,1), schedule_interval = '@daily', catchup = False
) as dag:
    None