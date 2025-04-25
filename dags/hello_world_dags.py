from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_world_local",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    schedule=None,  # Run manually
    tags=["example", "local"],
) as dag:
    hello_task = BashOperator(
        task_id="say_hello", 
        bash_command="echo 'Hello World from Local Airflow!'"
    )