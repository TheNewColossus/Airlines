# Airlines
This **Data Enginnering Project** grabs data from an airlines api, stores it in druid and makes it accessible to grafana visualisation software.

Get all the data related to your favourite flights at the click of a **button**.

## Table of Contents
### <ul> <li> [Architecture Diagram](#architecture-diagram) </ul>
### <ul> <li> [How it Works?](#how-it-works) </ul>

### Architecture Diagram
![](./images/Screenshot%20From%202025-01-02%2017-04-35.png)

### How it Works
**Aviations Stack** api is a free airlines api, which this project leverages to pull all the aviation data. Kafka cluster has been deployed using docker compose which produces messages using aviation stack's api and stores it in a topic named **Airlines_Data**. From there, these messages are then carted to **Apache Druid** which again has been hosted using docker and provides persistent storage for our aviation data. After that, visulaizing data using **Grafana**, a renowned open source BI/Visualization software, is extremely easy, which brings this project to its completion. 
