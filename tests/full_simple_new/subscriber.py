# -*- coding: UTF-8 -*-

'''
Module
    subscriber.py
Copyright
    Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    full_simple_new is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    full_simple_new is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines MQTT subscriber with attribute(s) and function(s).
'''

import sys
from typing import List

try:
    from paho.mqtt import client as mqtt_client
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2024, https://vroncevic.github.io/full_simple_new'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/full_simple_new/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

broker = 'broker.emqx.io'
port = 1883
topic = 'python/mqtt'
client_id = '89'
username = 'vroncevic'
password = 'mypassword'


def connect_mqtt(verbose=False) -> mqtt_client:
    '''
        Connects MQTT Client to broker.

        :param verbose: Enable/Disable verbose option
        :type verbose: <bool>
        :return: MQTT Client object
        :rtype: <Client>
        :exceptions: None
    '''
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected to MQTT broker!\n')
        else:
            print('Failed to connect, return code {0}!\n'.format(rc))
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    if verbose:
        print(
            'Connect client-id: {0} to broker {1} at port {2}\n'.format(
                client_id, broker, port
            )
        )
    return client


def subscribe_mqtt(client: mqtt_client, verbose=False):
    '''
        Subscribes client to a topic.

        :param client: MQTT Client object
        :type client: <Client>
        :param verbose: Enable/Disable verbose option
        :type verbose: <bool>
        :exceptions: None
    '''
    def on_message(client, userdata, msg):
        print(
            'Received {0} from {1} topic\n'.format(
                msg.payload.decode(), msg.topic
            )
        )
    client.subscribe(topic)
    client.on_message = on_message
    if verbose:
        print(
            'Subscribe client-id: {0} for topic {1}\n'.format(
                client_id, topic
            )
        )


def run_mqtt(verbose=False):
    '''
        Runs subscriber in MQTT service.

        :param verbose: Enable/Disable verbose option
        :type verbose: <bool>
        :exceptions: None
    '''
    client = connect_mqtt(verbose=verbose)
    subscribe_mqtt(client)
    client.loop_forever()


if __name__ == '__main__':
    run_mqtt(verbose=False)
