"""Arquivo que gera uma Dag que gera uma Xcom entre containers."""

from datetime import datetime

from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator


@dag(schedule_interval=None, start_date=datetime(2024, 5, 18), catchup=False)
def docker_testes_xcom():
    """Dag que gera nossa Exportação de datas."""

    @task
    def inicio():
        """Task Vazia para marcar início."""
        pass

    task1 = DockerOperator(
        docker_url="tcp://docker-socket-proxy:2375",
        container_name="gera_data",
        auto_remove=True,
        mount_tmp_dir=False,
        image="xcom-docker-operator:latest",
        task_id="gera_data",
        command="task1",
        force_pull=False,
        retrieve_output=True,
        retrieve_output_path="/tmp/script.out",  # nosec B108
    )

    @task
    def fim():
        """Task Vazia para marcar fim."""
        pass

    inicio() >> task1 >> fim()


dag = docker_testes_xcom()
