#!/bin/sh
export WORK_DIR=$(pwd)

# Conditional statement for setting workdir variable when the program boots for the first time
if grep -Fxq "WORKDIR=$WORK_DIR" ${WORK_DIR}/.env
then
    echo 
else
    sed -i "2iWORKDIR=$WORK_DIR" ${WORK_DIR}/.env
    # Postgres directory must be created right at the time the program first boots
    sudo mkdir -p ${WORK_DIR}/postgres
    # Grafana needs permission to write data to the directory
    sudo chmod -R 777 ${WORK_DIR}/grafana/storage
    sudo chmod -R 755 ${WORK_DIR}/druid
    sudo chmod -R 755 ${WORK_DIR}/postgres
fi
 
sudo docker compose up -d
