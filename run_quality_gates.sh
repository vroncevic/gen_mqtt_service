#!/bin/bash
#
# @brief   gen_mqtt_service
# @version 1.1.5
# @date    Sun Aug 09 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_mqtt_service
python3 gates/gates/isp_checker.py gen_mqtt_service
python3 gates/gates/limits_checker.py gen_mqtt_service
python3 gates/gates/srp_checker.py gen_mqtt_service

echo "Done"
