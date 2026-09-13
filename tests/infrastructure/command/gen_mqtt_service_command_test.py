# -*- coding: UTF-8 -*-

'''
Module
    gen_mqtt_service_command_test.py
Info
    Unit tests for GenMqttServiceCommandDefinition and GenMqttServiceCommandExecutor.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from gen_mqtt_service.core.model.project_setup import ProjectSetup
from gen_mqtt_service.core.service.iservice import IService
from gen_mqtt_service.infrastructure.command.gen_mqtt_service_command_definition import GenMqttServiceCommandDefinition
from gen_mqtt_service.infrastructure.command.gen_mqtt_service_command_executor import GenMqttServiceCommandExecutor


class TestGenMqttServiceCommand(TestCase):
    '''
        Tests for GenMqttServiceCommandDefinition and GenMqttServiceCommandExecutor.
    '''

    def test_definition(self) -> None:
        definition = GenMqttServiceCommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate MqttService project skeleton')
        self.assertEqual(len(definition.options), 5)
        opt_names = [opt.name for opt in definition.options]
        self.assertIn('--role', opt_names)
        self.assertIn('--scope', opt_names)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success_with_mapping(self) -> None:
        definition = GenMqttServiceCommandDefinition()
        executor = GenMqttServiceCommandExecutor(definition)

        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}

        params = {'name': 'test', 'output': '.', 'role': 'subscriber', 'scope': 'module'}
        result = executor.execute(params=params, service=mock_service)

        self.assertEqual(result['returncode'], 0)
        expected_setup = ProjectSetup(
            name='test',
            service_type='paho',
            role='subscriber',
            scope='module',
            output='.'
        )
        mock_service.execute.assert_called_once_with(params=expected_setup)

    def test_executor_execute_success_with_project_setup(self) -> None:
        definition = GenMqttServiceCommandDefinition()
        executor = GenMqttServiceCommandExecutor(definition)

        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}

        setup = ProjectSetup(
            name='demo_app',
            service_type='mosquitto',
            role='publisher',
            scope='demo',
            output='./out'
        )
        result = executor.execute(params=setup, service=mock_service)

        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=setup)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenMqttServiceCommandDefinition()
        executor = GenMqttServiceCommandExecutor(definition)

        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False

        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenMqttServiceCommandDefinition()
        executor = GenMqttServiceCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))

    def test_executor_get_definition(self) -> None:
        definition = GenMqttServiceCommandDefinition()
        executor = GenMqttServiceCommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)


if __name__ == '__main__':
    main()
