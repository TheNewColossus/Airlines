# Airlines
This **Data Enginnering Project** grabs data from an airlines api, stores it in druid and makes it accessible to grafana visualisation software.

Get all the data related to your favourite flights at the click of a **button**.

## Table of Contents
### <ul> <li> [Architecture Diagram](#architecture-diagram) </ul>
### <ul> <li> [How it Works?](#how-it-works) </ul>
### <ul> <li> [Prerequisites](#prerequisites) </ul>
### <ul> <li> [Running Project](#running-project) </ul>

### Architecture Diagram
![](./images/Screenshot%20From%202025-01-02%2017-04-35.png)

### How it Works
**Aviations Stack** api is a free airlines api, which this project leverages to pull all the aviation data. Kafka cluster has been deployed using docker compose which produces messages using aviation stack's api and stores it in a topic named **Airlines_Data**. From there, these messages are then carted to **Apache Druid** which again has been hosted using docker and provides persistent storage for our aviation data. After that, visulaizing data using **Grafana**, a renowned open source BI/Visualization software, is extremely easy, which brings this project to its completion. 

### Prerequisites
Software required to run the project. Install:
- [Docker](https://docs.docker.com/get-docker/) - You must allocate a minimum of 8 GB of Docker memory resource.
- [Python 3.10+ (pip)](https://www.python.org/)
- [docker-compose](https://docs.docker.com/compose/install/)

### Running Project
Shell scripts are a wrapper for `docker-compose` which work as a managing tool.

- Build project infrastructure
```sh
./start.sh
```

- Stop project infrastructure
```sh
./stop.sh
```

- Delete project infrastructure
```
./delete.sh
```
Do note that all the data will remain in the respective directories even after removing the compose cluster.
