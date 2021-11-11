#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     gen_mqtt_service_run.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_mqtt_service is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_mqtt_service is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Main entry point of tool gen_mqtt_service.
'''

import sys

try:
    from gen_mqtt_service import GenMQTTService
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://github.com/vroncevic/gen_mqtt_service'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_mqtt_service/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

if __name__ == '__main__':
    TOOL = GenMQTTService(verbose=False)
    TOOL.process(verbose=False)
