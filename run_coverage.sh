#!/bin/bash
#
# @brief   gen_mqtt_service
# @version 1.1.5
# @date    Sun Aug 09 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_mqtt_service
pylint gen_mqtt_service > gen_mqtt_service.report
echo "Done"
