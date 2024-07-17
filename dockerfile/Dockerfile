FROM apache/airflow:2.9.2-python3.8 as images_test

USER root

# Remove unnecessary packages and clean, then update and install required packages
RUN apt-get autoremove -yqq --purge && apt-get clean && \
    apt-get update && apt-get -y upgrade && \
    apt-get -y install default-libmysqlclient-dev gcc gnupg wget

# Switch to airflow user to install Python packages
USER airflow

RUN pip install mysqlclient
RUN pip install pymongo

# Copy DAGs
COPY --chown=airflow:root dags /opt/airflow/dags
