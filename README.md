# Flow Backend

The Apache Airflow backend for the web service. The individual services are run within Docker containers, the majority of which are for Apache Airflow. A Flask web server is embedded to expose the PostgreSQL database through a GraphQL interface, and `pgadmin4` is included for easy manipulation of the database through a visual interface.

## How to run

```bash
docker-compose up
```