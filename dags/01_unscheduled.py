import datetime as dt
from pathlib import Path
from textwrap import dedent

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="01_unscheduled",
    description="A simple DAG",
    start_date=dt.datetime(2022,2,25),
    schedule_interval=None) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3
    )

    t1.doc_md = dedent(
        """
        ### Task documentation
        """
    )

    dag.doc_md = __doc__
    dag.doc_md = """
    This is a documentation that can be placed anywhere.
    """

    templated_command= dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
    )
    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=templated_command
    )

