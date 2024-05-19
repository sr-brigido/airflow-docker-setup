# Apache Airflow em Docker com Docker-proxy
Repositório contendo o necessário para rodar o [`Apache Airflow`](https://airflow.apache.org/docs/) localmente em Docker com o recurso de *Docker-proxy* para execução de container docker na maquina host.

>Versão 1.0.0 | Autor: Gabriel Ronchi Brigido

## Pré-requisitos
- Para o versionamento e reastreabiliade do código use o **Git**, instalação [aqui](https://git-scm.com)
- Para edição facilitada do código use o **VSCode**, instalação [aqui](https://code.visualstudio.com/)
- Para melhor controle de versões de instalação do *Python* use o **Pyenv**, guia de instalação [aqui](https://www.youtube.com/watch?v=HTx18uyyHw8). Este projeto utiliza **Python 3.12.3**
- Para gerenciamento de pacotes de dependências use o **Poetry**, consulte a  documentação [aqui](https://python-poetry.org/docs/)
- Para o ambiente de testes local, precisa-se utilizar o **Docker**, consulte a documentação [aqui](https://docs.docker.com/)

## Subindo Airflow localmente
Siga os passos para executar o Airflow de maneira correta:

- Clone o repositório:

```bash
git clone ttps://github.com/sr-brigido/airflow-docker-setup.git
cd airflow-docker-setup     #Navegue até a pasta do projeto
```

 - Caso você esteja utilizando **linux**, você precisa declarar uma variável de ambiente contendo o id do usuário logado ou utilizar o seguinte comando para exportar o id em um arquivo `.env`:

```bash
echo "AIRFLOW_UID=$(id -u)" > .env
```

- Se estiver utilizando **windows**, basta renomear o arquivo `exemplo.env` para `.env`

Após isso, vamos executar os comandos padrão de *setup* do Airflow:

```bash
docker-compose up airflow-init  #setup inicial do Airflow
```

```bash
docker-compose up -d    #Subindo o restante dos serviços
```

Quando os serviços estiverem rodando você pode acessar a UI do Airflow em [http://localhost:8080](http://localhost:8080)

## Ajustando o ambiente para construção de DAGs

Execute os comandos com `Poetry` para instalar as bibliotecas do projeto

```bash
poetry config virtualenvs.in-project true   #Comando para criar os ambientes virtuais dentro do projeto
poetry config virtualenvs.prefer-active-python true #Comando para o poetry identificar a versão do python utilizada do projeto
```
```bash
poetry install --no-root    #instalar as dependencias base do projeto
```
