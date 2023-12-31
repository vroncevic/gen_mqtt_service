#!/bin/bash
#
# @brief   gen_mqtt_service
# @version v1.1.1
# @date    Sat Aug 1 07:52:38 2020
# @company None, free software to use 2020
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf fresh_new/ full_simple_new/ latest_pro/ simple_read/ simple_write/
python3 -m coverage run -m --source=../gen_mqtt_service unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
