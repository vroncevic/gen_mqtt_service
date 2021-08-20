<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/gen_mqtt_service_logo.png" width="25%">

# Generate MQTT Service

**gen_mqtt_service** is toolset for generation of MQTT service.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_mqtt_service/workflows/Python%20package%20gen_mqtt_service/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_mqtt_service.svg)](https://github.com/vroncevic/gen_mqtt_service/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_mqtt_service.svg)](https://github.com/vroncevic/gen_mqtt_service/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of MQTT service](#generation-flow-of-mqtt-service)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![Development environment](https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/debtux.png)

![Install Python2 Package](https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python2%20Package%20gen_mqtt_service/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python3%20Package%20gen_mqtt_service/badge.svg?branch=master)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen-mqtt-service/)**.

You can install by using pip
```
# python2
pip install gen-mqtt-service
# python3
pip3 install gen-mqtt-service
```

##### Install using setuptools

Navigate to release **[page](https://github.com/vroncevic/gen_mqtt_service/releases/)** download and extract release archive.

To install **gen_mqtt_service** type the following:
```
tar xvzf gen_mqtt_service-x.y.z.tar.gz
cd gen_mqtt_service-x.y.z/
# python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use docker to create image/container.

[![gen_mqtt_service docker checker](https://github.com/vroncevic/gen_mqtt_service/workflows/gen_mqtt_service%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_mqtt_service/actions?query=workflow%3A%22gen_mqtt_service+docker+checker%22)

### Dependencies

**gen_mqtt_service** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Generation flow of MQTT service

Base flow of generation process:

![MQTT generation flow](https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/gen_mqtt_service_flow.png)

### Tool structure

**gen_mqtt_service** is based on OOP.

Generator structure:

```
gen_mqtt_service/
├── conf/
│   ├── gen_mqtt_service.cfg
│   ├── gen_mqtt_service_util.cfg
│   ├── project.yaml
│   └── template/
│       ├── mosquitto/
│       │   ├── publisher.template
│       │   └── subscriber.template
│       ├── mqtt_node/
│       │   ├── publisher.template
│       │   └── subscriber.template
│       ├── mqtt_node_ws/
│       │   ├── client.template
│       │   └── server.template
│       ├── paho/
│       │   ├── publisher.template
│       │   └── subscriber.template
│       ├── template_mosquitto.yaml
│       ├── template_mqtt_node_ws.yaml
│       ├── template_mqtt_node.yaml
│       └── template_paho.yaml
├── __init__.py
├── log/
│   └── gen_mqtt_service.log
├── pro/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── pro_name.py
│   │   ├── pro_selector.py
│   │   └── pro_type.py
│   ├── __init__.py
│   ├── read_template.py
│   └── write_template.py
└── run/
    └── gen_mqtt_service_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen-mqtt-service/badge/?version=latest)](https://gen-mqtt-service.readthedocs.io/en/latest/?badge=latest)

More documentation and info at:
* [gen-mqtt-service.readthedocs.io](https://gen-mqtt-service.readthedocs.io/en/latest)
* [MQTT Service](overview.md)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2020 by [vroncevic.github.io/gen_mqtt_service](https://vroncevic.github.io/gen_mqtt_service)

**gen_mqtt_service** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
