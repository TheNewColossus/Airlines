#!/bin/sh
export WORK_DIR=$(pwd)

# Conditional statement for setting workdir variable when the program boots for the first time
if grep -Fxq "WORKDIR=$WORK_DIR" ${WORK_DIR}/.env
then
    echo 
else
    sed -i "1iWORKDIR=$WORK_DIR" ${WORK_DIR}/.env
fi

# Grafana needs permission to write data to the directory
sudo chmod -R 777 ${WORK_DIR}/grafana/storage
 
sudo docker compose up -d
