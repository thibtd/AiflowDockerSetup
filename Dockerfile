ARG AIRFLOW_VERSION=2.10.4 # Use a specific stable version
FROM apache/airflow:${AIRFLOW_VERSION}


# Install base Airflow and requirements if file exists
RUN \
    pip install apache-airflow==${AIRFLOW_VERSION} && \
    if [ -f requirements.txt ]; then \
        pip install -r requirements.txt; \
    fi