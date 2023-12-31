# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
 Copyright
     Copyright (C) 2020 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for read a template files and return a content.
'''

import sys
from os.path import isdir, dirname, realpath

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, https://vroncevic.github.io/gen_mqtt_service'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_mqtt_service/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for read a template files and return a content.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | TEMPLATE_DIR - template dir path.
                | __template_dir - absolute file path of template dir.
            :methods:
                | __init__ - initial constructor.
                | get_template_dir - getter for template directory object.
                | read - read a template and return a string representation.
                | __str__ - dunder method for ReadTemplate.
    '''

    GEN_VERBOSE = 'GEN_MQTT_SERVICE::PRO::READ_TEMPLATE'
    TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'init reader')
        template_dir = '{0}{1}'.format(
            dirname(realpath(__file__)), ReadTemplate.TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def get_template_dir(self):
        '''
            Getter for template directory.

            :return: template directory path | None.
            :rtype: <str> | <NoneType>
        '''
        return self.__template_dir

    def read(self, template_modules, verbose=False):
        '''
            Read template structure.

            :param template_modules: template modules - configuration.
            :type template_modules: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template content for setup module | empty list.
            :rtype: <list>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:template_modules', template_modules)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        setup_content, template_file = [], None
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'load templates')
        template_file = '{0}{1}'.format(self.__template_dir, template_modules)
        self.check_path(template_file, verbose=verbose)
        self.check_mode('r', verbose=verbose)
        self.check_format(template_file, 'yaml', verbose=verbose)
        if self.is_file_ok():
            yml2obj = Yaml2Object(template_file)
            configuration = yml2obj.read_configuration()
            templates = configuration['templates']
            modules = configuration['modules']
            for template, module in zip(templates, modules):
                template_path = '{0}{1}'.format(self.__template_dir, template)
                with open(template_path, 'r') as setup_template:
                    setup_content.append({module: setup_template.read()})
        return setup_content

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            self.__template_dir
        )
