FROM python:3.8.1-slim-buster

RUN apt-get update && apt-get install -qq -y \
    git gcc build-essential libpq-dev --fix-missing --no-install-recommends \ 
    && apt-get clean

WORKDIR /dbt

COPY models models
COPY dbt_project.yml dbt_project.yml
COPY profiles.yml profiles.yml

# Install the dbt Postgres adapter. This step will also install dbt-core
RUN pip install --upgrade pip
RUN pip install dbt-core
RUN pip install dbt-postgres
