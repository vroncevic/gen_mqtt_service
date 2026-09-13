# -*- coding: UTF-8 -*-

'''
Module
    project_setup_test.py
Info
    Unit tests for ProjectSetup class.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_mqtt_service.core.model.project_setup import ProjectSetup


class TestProjectSetup(TestCase):
    '''
        Tests for ProjectSetup domain model.
    '''

    def test_project_setup_initialization(self) -> None:
        '''
            Tests initialization and attribute values of ProjectSetup.
        '''
        setup = ProjectSetup(
            name='myapp',
            service_type='paho',
            role='subscriber',
            scope='module',
            output='/tmp/out'
        )
        self.assertEqual(setup.name, 'myapp')
        self.assertEqual(setup.service_type, 'paho')
        self.assertEqual(setup.role, 'subscriber')
        self.assertEqual(setup.scope, 'module')
        self.assertEqual(setup.output, '/tmp/out')

    def test_project_setup_to_dict(self) -> None:
        '''
            Tests dictionary representation of ProjectSetup.
        '''
        setup = ProjectSetup(
            name='myapp',
            service_type='mosquitto',
            role='both',
            scope='demo',
            output='./demo'
        )
        expected = {
            'name': 'myapp',
            'service_type': 'mosquitto',
            'role': 'both',
            'scope': 'demo',
            'output': './demo'
        }
        self.assertEqual(setup.to_dict(), expected)


if __name__ == '__main__':
    main()
