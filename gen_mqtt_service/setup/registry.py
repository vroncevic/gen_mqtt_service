# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_mqtt_service is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_mqtt_service is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Encapsulates core gen_mqtt_service components for simplification of gen_mqtt_service bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_mqtt_service.core.service.iservice import IService
from gen_mqtt_service.core.service.isubprocessor import ISubProcessor
from gen_mqtt_service.infrastructure.cli.icli import ICLI
from gen_mqtt_service.setup.bundle import GenMqttServiceBundle
from gen_mqtt_service.setup.validator import GenMqttServiceBundleValidator
from gen_mqtt_service.setup.keys import GenMqttServiceBundleKeys
from gen_mqtt_service.setup.dependencies import GenMqttServiceBundleDependencies
from gen_mqtt_service.setup.dep_validator import GenMqttServiceBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_mqtt_service'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_mqtt_service/blob/dev/LICENSE'
__version__ = '1.1.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenMqttServiceBundleRegistry:
    '''
        Encapsulates core gen_mqtt_service components for simplification of gen_mqtt_service bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_mqtt_service bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenMqttServiceBundleDependencies) -> GenMqttServiceBundle:
        '''
            Creates the gen_mqtt_service bundle.

            :param dependencies: The gen_mqtt_service bundle dependencies.
            :return: The gen_mqtt_service bundle.
            :exceptions:
                | ATSValueError: The gen_mqtt_service bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_mqtt_service bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_mqtt_service bundle must be provided and have proper values.
                | ATSTypeError:  The gen_mqtt_service bundle must be an instance of GenMqttServiceBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenMqttServiceBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenMqttServiceBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenMqttServiceBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenMqttServiceBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenMqttServiceBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenMqttServiceBundle = GenMqttServiceBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenMqttServiceBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
