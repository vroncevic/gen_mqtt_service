# -*- coding: UTF-8 -*-

'''
Module
    subprocessor_test.py
Info
    Unit tests for SubProcessor adapter.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock, patch

from gen_mqtt_service.core.model.project_setup import ProjectSetup
from gen_mqtt_service.infrastructure.subprocessor import SubProcessor


class DummyLogger:
    '''
        Dummy logger for unit testing.
    '''

    def write_log(self, level: int, message: str) -> None:
        pass


class DummyContext:
    '''
        Dummy context holding dummy logger.
    '''

    def __init__(self) -> None:
        self.logger = DummyLogger()


class DummyGenerator:
    '''
        Dummy generator implementing IGeneratorManager protocol structurally.
    '''

    def get_context(self) -> DummyContext:
        return DummyContext()

    def generate(self, data: object) -> bool:
        return True

    def is_initialized(self) -> bool:
        return True

    def get_bundle(self) -> object:
        return None

    def update_bundle(self, bundle: object) -> None:
        pass

    def prepare_template_values(self) -> dict[str, object]:
        return {}

    def __str__(self) -> str:
        return "DummyGenerator"


class TestSubProcessor(TestCase):
    '''
        Tests for SubProcessor adapter.
    '''

    def test_init_success(self) -> None:
        generator = DummyGenerator()
        sub = SubProcessor(generator)
        self.assertEqual(sub._generator, generator)

    def test_init_errors(self) -> None:
        with self.assertRaises(Exception):
            SubProcessor(None)
        with self.assertRaises(Exception):
            SubProcessor("invalid_generator")

    @patch('gen_mqtt_service.infrastructure.subprocessor.walk')
    def test_run_success_with_mapping(self, mock_walk: Mock) -> None:
        mock_walk.return_value = [
            ('/tmp/out', [], ['file.txt']),
            ('/tmp/out/sub', [], ['another_file.txt'])
        ]
        generator = DummyGenerator()
        generator.generate = Mock(return_value=True)

        sub = SubProcessor(generator)
        params = {'output': '/tmp/out', 'name': 'test_project'}
        result = sub.run(params=params)

        self.assertEqual(result['returncode'], 0)
        self.assertIn('success', result['stdout'])
        generator.generate.assert_called_once()

    @patch('gen_mqtt_service.infrastructure.subprocessor.walk')
    def test_run_success_subscriber_module(self, mock_walk: Mock) -> None:
        mock_walk.return_value = [('/tmp/out', [], ['subscriber.py'])]
        generator = DummyGenerator()
        generator.generate = Mock(return_value=True)

        sub = SubProcessor(generator)
        setup = ProjectSetup(
            name='sub_app',
            service_type='paho',
            role='subscriber',
            scope='module',
            output='/tmp/out'
        )
        result = sub.run(params=setup)

        self.assertEqual(result['returncode'], 0)
        self.assertIn('success', result['stdout'])
        generator.generate.assert_called_once()

    @patch('gen_mqtt_service.infrastructure.subprocessor.walk')
    def test_run_success_publisher_demo(self, mock_walk: Mock) -> None:
        mock_walk.return_value = [('/tmp/out', [], ['publisher.c'])]
        generator = DummyGenerator()
        generator.generate = Mock(return_value=True)

        sub = SubProcessor(generator)
        setup = ProjectSetup(
            name='pub_app',
            service_type='mosquitto',
            role='publisher',
            scope='demo',
            output='/tmp/out'
        )
        result = sub.run(params=setup)

        self.assertEqual(result['returncode'], 0)
        self.assertIn('success', result['stdout'])
        generator.generate.assert_called_once()

    def test_run_failure(self) -> None:
        generator = DummyGenerator()
        generator.generate = Mock(return_value=False)

        sub = SubProcessor(generator)
        params = {'output': '/tmp/out', 'name': 'test_project'}
        result = sub.run(params=params)

        self.assertEqual(result['returncode'], 1)
        self.assertIn('failed', result['stderr'])

    def test_run_exception(self) -> None:
        generator = DummyGenerator()
        generator.generate = Mock(side_effect=RuntimeError('error'))

        sub = SubProcessor(generator)
        params = {'output': '/tmp/out', 'name': 'test_project'}
        result = sub.run(params=params)

        self.assertEqual(result['returncode'], 1)
        self.assertIn('failed', result['stderr'])

    def test_is_initialized(self) -> None:
        generator = DummyGenerator()
        generator.is_initialized = Mock(return_value=True)

        sub = SubProcessor(generator)
        self.assertTrue(sub.is_initialized())
        generator.is_initialized.assert_called_once()

    def test_str_representation(self) -> None:
        generator = DummyGenerator()
        sub = SubProcessor(generator)
        self.assertTrue(isinstance(str(sub), str))


if __name__ == '__main__':
    main()
