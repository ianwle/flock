FROM debian:latest

RUN apt update && apt install python3 pip -y
RUN python3 -m pip install apache-airflow --ignore-installed six
# RUN pip install -r requirements.txt
RUN python3 -m pip install newsapi-python
RUN export AIRFLOW_HOME=~/airflow

EXPOSE 8080

# CMD ["python3 -m airflow standalone"]
# RUN sh