# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenMqttServiceBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_mqtt_service.setup.bundle import GenMqttServiceBundle
from gen_mqtt_service.setup.factory import GenMqttServiceBundleFactory


class TestGenMqttServiceBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenMqttServiceBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenMqttServiceBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_mqtt_service/infrastructure/config/gen_mqtt_service.cfg'}
        bundle = GenMqttServiceBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenMqttServiceBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenMqttServiceBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenMqttServiceBundleFactory.get_version(), '1.1.5')
