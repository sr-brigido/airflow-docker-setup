"""Arquivo para DAGs que testam o DockerOperator."""

from datetime import datetime

from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator


@dag(schedule_interval=None, start_date=datetime(2024, 5, 18), catchup=False)
def docker_operator_teste():
    """Dag para execução de teste do DockerOperator."""

    @task
    def inicio():
        """Task Vazia para marcar início."""
        pass

    task1 = DockerOperator(
        docker_url="tcp://docker-socket-proxy:2375",
        container_name="printa_teste",
        auto_remove=True,
        mount_tmp_dir=False,
        image="python:3.12.3-slim",
        task_id="printa_teste",
        command='echo "opa, to rodando dentro de um container"',
        force_pull=False,
    )

    @task
    def fim():
        """Task Vazia para marcar fim."""
        pass

    inicio() >> task1 >> fim()


dag = docker_operator_teste()
