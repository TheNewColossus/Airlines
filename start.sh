#!/bin/sh
export WORK_DIR=$(pwd);

# Grafan needs permission to write data to the directory
sudo chmod -R 777 ${WORK_DIR}/grafana/storage
 
sudo docker compose up -d