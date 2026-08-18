# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenMqttServiceBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_mqtt_service.setup.keys import GenMqttServiceBundleKeys


class TestGenMqttServiceBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenMqttServiceBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenMqttServiceBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenMqttServiceBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenMqttServiceBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenMqttServiceBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenMqttServiceBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenMqttServiceBundleKeys.OPTION_INFO_FILE, opts)
