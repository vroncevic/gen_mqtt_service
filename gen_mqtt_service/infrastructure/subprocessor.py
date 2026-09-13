# -*- coding: UTF-8 -*-

'''
Module
    subprocessor.py
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
    Defines sub-processor adapter implementing ISubProcessor.
'''

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from json import loads
from logging import INFO
from os import walk
from os.path import dirname, realpath, relpath

from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.generation.data import GeneratorData
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.reflection import to_str

from gen_mqtt_service.core.model.project_setup import ProjectSetup

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_mqtt_service'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_mqtt_service/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SubProcessor:
    '''
        Adapter that executes sub-processes.

        It defines:

            :attributes:
                | _scheme - Path to the scheme json file.
                | _templates - Path to the templates tgz file.
                | _generator - Generator manager used to generate code from templates.
                | _logger - Logger used to log messages.
            :methods:
                | run - Executes a sub-process.
                | is_initialized - Checks if the subprocessor is initialized.
                | __str__ - Returns the SubProcessor as string representation.
    '''

    _scheme: str = 'config/scheme.json'
    _templates: str = 'config/templates.tgz'
    _generator: IGeneratorManager
    _logger: ILogger

    def __init__(self, generator: IGeneratorManager) -> None:
        '''
            Initializes the SubProcessor adapter.

            :param generator: The generator manager.
            :exceptions:
                | ATSValueError: The generator must be provided.
                | ATSTypeError:  The generator must be an instance of IGenerator.
        '''
        ctx: str = 'subprocessor::init(...)'
        msg_generator_none: str = 'the generator must be provided'
        msg_generator_istype: str = f'the generator must be an instance of {IGeneratorManager.__name__}'

        not_none(generator, ctx, msg_generator_none)
        istype(generator, IGeneratorManager, ctx, msg_generator_istype)

        self._generator = generator
        self._logger = generator.get_context().logger

    def _build_scheme(
        self,
        *,
        scheme_path: str,
        service_type: str,
        role: str,
        scope: str
    ) -> Mapping[str, object]:
        '''
            Builds dynamic scheme with role and scope exclusions.

            :param scheme_path: Path to base scheme configuration file.
            :param service_type: Type of service.
            :param role: Generation role (subscriber, publisher, both).
            :param scope: Generation scope (module, demo).
            :return: Resolved scheme configuration dictionary.
            :exceptions: None.
        '''
        with open(scheme_path, 'r', encoding='utf-8') as scheme_file:
            scheme_data: dict[str, dict[str, object]] = loads(scheme_file.read())

        if service_type in scheme_data:
            type_config: dict[str, object] = dict(scheme_data[service_type])
            base_exclude: list[str] = list(type_config.get('exclude', []))
            base_exclude.append('*client.js*')

            if role == 'subscriber':
                base_exclude.extend(['*publisher*', '*run_publisher*'])
            elif role == 'publisher':
                base_exclude.extend(['*subscriber*', '*run_subscriber*'])

            if scope == 'module':
                base_exclude.extend([
                    '*Makefile*',
                    '*CMakeLists.txt*',
                    '*package.json*',
                    '*requirements.txt*',
                    '*README.md*',
                    '*docker-compose.yml*',
                    '*server.js*',
                    '*main.py*',
                    '*.sh*'
                ])

            type_config['exclude'] = base_exclude
            scheme_data[service_type] = type_config

        return scheme_data

    def run(self, *, params: Mapping[str, object] | ProjectSetup) -> Mapping[str, object]:
        '''
            Executes the generator.

            :param params: The command parameters for generator or ProjectSetup.
            :return: Return code, stdout and stderr messages.
            :exceptions: None.
        '''
        try:
            output_dir: str = (
                params.output if isinstance(params, ProjectSetup)
                else str(params.get('output', './'))
            )
            project_name: str = (
                params.name if isinstance(params, ProjectSetup)
                else str(params.get('name', 'myapp'))
            )
            service_type: str = (
                params.service_type if isinstance(params, ProjectSetup)
                else str(params.get('type', params.get('service_type', 'paho')))
            )
            role: str = (
                params.role if isinstance(params, ProjectSetup)
                else str(params.get('role', 'both'))
            )
            scope: str = (
                params.scope if isinstance(params, ProjectSetup)
                else str(params.get('scope', 'demo'))
            )

            scheme_path: str = f'{dirname(realpath(__file__))}/{self._scheme}'
            templates: str = f'{dirname(realpath(__file__))}/{self._templates}'

            scheme_data = self._build_scheme(
                scheme_path=scheme_path,
                service_type=service_type,
                role=role,
                scope=scope
            )

            success = self._generator.generate(
                data=GeneratorData(
                    archive_path=templates,
                    target_dir=output_dir,
                    template_key=service_type,
                    scheme=scheme_data,
                    template_values={
                        'project_name': project_name,
                        'PRO': project_name,
                        'YEAR': str(datetime.now().year),
                        'ROLE': role,
                        'SCOPE': scope
                    }
                )
            )

            if success:
                self._logger.write_log(INFO, '    Generated files:')

                for root, _, files in walk(output_dir):
                    for file in files:
                        rel_dir = relpath(root, output_dir)

                        if rel_dir == '.':
                            self._logger.write_log(INFO, f'      {file}')
                        else:
                            self._logger.write_log(INFO, f'      {rel_dir}/{file}')

            return {
                'returncode': 0 if success else 1,
                'stdout': f'{project_name} skeleton successfully generated.' if success else '',
                'stderr': f'failed to generate {project_name} skeleton.' if not success else ''
            }

        except Exception as exc:
            return {'returncode': 1, 'stdout': '', 'stderr': f'failed to generate {exc}'}

    def is_initialized(self) -> bool:
        '''
            Checks if the subprocessor is initialized.

            :return: True if the subprocessor is initialized, False otherwise.
            :exceptions: None.
        '''
        return self._generator.is_initialized()

    def __str__(self) -> str:
        '''
            Returns the SubProcessor as string representation.

            :return: The SubProcessor as string representation.
            :exceptions: None.
        '''
        return to_str(self)
