#!/bin/bash
export WORK_DIR=$(pwd);

read -p "Press '1' to pause the cluster or '2' to resume it: " resp

case $resp in

  1)
    echo -e "\nPausing the docker cluster\n"
    sudo docker compose stop
    ;;

  2)
    echo -e "\nResuming the docker cluster\n"
    sudo docker compose start
    ;;

  *)
    echo -e "\nWrong input\n"
    ;;
esac
