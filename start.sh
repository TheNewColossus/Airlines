#!/bin/sh
export WORK_DIR=$(pwd)

# Conditional statement for setting workdir variable when the program boots for the first time
if grep -Fxq "WORKDIR=$WORK_DIR" ${WORK_DIR}/.env
then
    echo 
else
    sed -i "1iWORKDIR=$WORK_DIR" ${WORK_DIR}/.env

    # Grafana needs permission to write data to the directory
    sudo chmod -R 777 ${WORK_DIR}/grafana/storage
    sudo chmod -R 777 ${WORK_DIR}/druid
    sudo chmod -R 777 ${WORK_DIR}/zookeeper
    sudo chmod -R 777 ${WORK_DIR}/postgres
fi
 
sudo docker compose up -d
