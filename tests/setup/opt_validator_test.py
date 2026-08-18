# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenMqttServiceBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_mqtt_service.setup.opt_validator import GenMqttServiceBundleOptionsValidator


class TestGenMqttServiceBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenMqttServiceBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenMqttServiceBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenMqttServiceBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenMqttServiceBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenMqttServiceBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenMqttServiceBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenMqttServiceBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenMqttServiceBundleOptionsValidator.is_valid({'info_file': 123}))
