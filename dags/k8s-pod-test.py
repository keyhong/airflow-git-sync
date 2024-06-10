from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)
from airflow.utils.dates import days_ago
import os

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}

with DAG(
    dag_id="example_kubernetes_pod_operator",
    default_args=default_args,
    schedule_interval=None,
    tags=["example"],
) as dag:

    k = KubernetesPodOperator(
        name="hello-dry-run",
        image="ubuntu:22.04",
        cmds=["bash", "-cx"],
        arguments=["sleep 10"],
        labels={"foo": "bar"},
        task_id="dry_run_demo",
        get_logs=True,
        is_delete_operator_pod=True,
        do_xcom_push=True,
    )

    k
