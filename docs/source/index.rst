Generate MQTT Service
----------------------

**gen_mqtt_service** is toolset for generation MQTT service.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python2%20Package%20gen_mqtt_service/badge.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python2%20Package%20gen_mqtt_service/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_mqtt_service.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_mqtt_service.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_mqtt_service/badge/?version=latest
   :target: https://gen_mqtt_service.readthedocs.io/projects/gen_mqtt_service/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   modules
   self

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python2%20Package%20gen_mqtt_service/badge.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python2%20Package%20gen_mqtt_service/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python3%20Package%20gen_mqtt_service/badge.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/workflows/Install%20Python3%20Package%20gen_mqtt_service/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_mqtt_service/releases

To install **gen_mqtt_service** type the following

.. code-block:: bash

    tar xvzf gen_mqtt_service-x.y.z.tar.gz
    cd gen_mqtt_service-x.y.z/
    # python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_data
    python setup.py install_egg_info
    # pyton3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_data
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton2
    pip install gen-mqtt-service
    # pyton3
    pip3 install gen-mqtt-service

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_mqtt_service/workflows/gen_mqtt_service%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/actions?query=workflow%3A%22gen_mqtt_service+docker+checker%22

Dependencies
-------------

**gen_mqtt_service** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Generation flow of MQTT service
---------------------------------

Base flow of generation process

.. image:: https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/gen_mqtt_service_flow.png

Tool structure
---------------

**gen_mqtt_service** is based on OOP.

Code structure

.. code-block:: bash

    gen_mqtt_service/
    ├── conf/
    │   ├── gen_mqtt_service.logo
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

Copyright and licence
-----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2020 by `vroncevic.github.io/gen_mqtt_service <https://vroncevic.github.io/gen_mqtt_service>`_

**gen_mqtt_service** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
