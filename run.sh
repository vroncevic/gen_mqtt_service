#!/usr/bin/env bash

python3 main.py create --name "my_mosquitto" --type "mosquitto" --output "./demo/mosquitto"
python3 main.py create --name "my_node" --type "node" --output "./demo/node"
python3 main.py create --name "my_node_ws" --type "node_ws" --output "./demo/node_ws"
python3 main.py create --name "my_paho" --type "paho" --output "./demo/paho"
