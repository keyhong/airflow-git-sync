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
        namespace="default",
        image="ubuntu:22.04",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        name="airflow-test-pod",
        task_id="pod_task",
        get_logs=True,
        in_cluster=False,
        config_file="/home/airflow/.kube/config",
    )

    k
