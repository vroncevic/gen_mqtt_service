#!/bin/bash
#
# @brief   gen_mqtt_service
# @version 1.1.5
# @date    Sun Aug 09 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 main.py create --name "my_mosquitto" --type "mosquitto" --output "./demo/mosquitto"
python3 main.py create --name "my_node" --type "node" --output "./demo/node"
python3 main.py create --name "my_node_ws" --type "node_ws" --output "./demo/node_ws"
python3 main.py create --name "my_paho" --type "paho" --output "./demo/paho"
