#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2020 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_mqtt_service is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_mqtt_service is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines setup for tool gen_mqtt_service.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_mqtt_service'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_mqtt_service/blob/dev/LICENSE'
__version__: str = '1.1.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR = 'gen_mqtt_service/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS
setup(
    name='gen_mqtt_service',
    version='1.1.4',
    description='Generating MQTT modules',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_mqtt_service',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, MQTT, Modules',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_mqtt_service', 'gen_mqtt_service.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_mqtt_service': [
            'py.typed',
            f'{CONF}/gen_mqtt_service.logo',
            f'{CONF}/gen_mqtt_service.cfg',
            f'{CONF}/gen_mqtt_service_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/mosquitto/publisher.template',
            f'{TEMPLATE}/mosquitto/subscriber.template',
            f'{TEMPLATE}/node/publisher.template',
            f'{TEMPLATE}/node/subscriber.template',
            f'{TEMPLATE}/node_ws/client.template',
            f'{TEMPLATE}/node_ws/server.template',
            f'{TEMPLATE}/paho/publisher.template',
            f'{TEMPLATE}/paho/subscriber.template',
            f'{LOG}/gen_mqtt_service.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_mqtt_service_run.py'
        ]
    )]
)
