#!/bin/sh
export WORK_DIR=$(pwd);
sudo docker buildx build -t grafana/grafana-enterprise ${WORK_DIR}/grafana/
docker-compose up -d