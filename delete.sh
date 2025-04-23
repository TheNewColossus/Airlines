#!/bin/bash
export WORK_DIR=$(pwd);

sudo docker compose down
sudo docker system prune -avf