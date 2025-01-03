# Airlines
This **Data Enginnering Project** grabs data from an airlines api, stores it in druid and makes it accessible to grafana visualisation software.

Get all the data related to your favourite flights at the click of a **button**.

## Table of Contents
### <ul> <li> [Architecture Diagram](#architecture-diagram) </ul>
### <ul> <li> [How it Works?](#how-it-works) </ul>
### <ul> <li> [Prerequisites](#prerequisites) </ul>
### <ul> <li> [Running Project](#running-project) </ul>
### <ul> <li> [Contact](#contact) </ul>

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
Shell scripts are wrappers for `docker-compose` which works as a managing tool in this project.

- Build project infrastructure
```
./start.sh
```

- Stop project infrastructure
```
./stop.sh
```

- Delete project infrastructure
```
./delete.sh
```
Do note that all the data will remain in the respective directories even after removing the compose cluster. This design decision is deliberate as persistent storage is favoured in almost every organizational setting.

### Contact
Feel free to reach out to me regarding this project. Thanks!!!  <ins>Aayushh Dutta</ins>
