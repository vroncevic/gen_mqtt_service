Generate MQTT Service
----------------------

**gen_mqtt_service** is toolset for generation MQTT service.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_mqtt_service python checker| |gen_mqtt_service python package| |github issues| |documentation status| |github contributors|

.. |gen_mqtt_service python checker| image:: https://github.com/vroncevic/gen_mqtt_service/actions/workflows/gen_mqtt_service_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/actions/workflows/gen_mqtt_service_python_checker.yml

.. |gen_mqtt_service python package| image:: https://github.com/vroncevic/gen_mqtt_service/actions/workflows/gen_mqtt_service_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/actions/workflows/gen_mqtt_service_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_mqtt_service.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_mqtt_service.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_mqtt_service/badge/?version=latest
   :target: https://gen-mqtt-service.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_mqtt_service python3 build|

.. |gen_mqtt_service python3 build| image:: https://github.com/vroncevic/gen_mqtt_service/actions/workflows/gen_mqtt_service_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_mqtt_service/actions/workflows/gen_mqtt_service_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_mqtt_service/releases

To install **gen_mqtt_service** type the following

.. code-block:: bash

    tar xvzf gen_mqtt_service-x.y.z.tar.gz
    cd gen_mqtt_service-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_mqtt_service-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_mqtt_service_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_mqtt_service_run.py /usr/local/bin/gen_mqtt_service_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen-mqtt-service

Dependencies
-------------

**gen_mqtt_service** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_mqtt_service** is based on OOP.

Code structure

.. code-block:: bash

    gen_mqtt_service/
        ├── conf/
        │   ├── gen_mqtt_service.cfg
        │   ├── gen_mqtt_service.logo
        │   ├── gen_mqtt_service_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── mosquitto/
        │       │   ├── publisher.template
        │       │   └── subscriber.template
        │       ├── node/
        │       │   ├── publisher.template
        │       │   └── subscriber.template
        │       ├── node_ws/
        │       │   ├── client.template
        │       │   └── server.template
        │       └── paho/
        │           ├── publisher.template
        │           └── subscriber.template
        ├── __init__.py
        ├── log/
        │   └── gen_mqtt_service.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_mqtt_service_run.py
        
        10 directories, 18 files

Copyright and licence
-----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2020 - 2026 by `vroncevic.github.io/gen_mqtt_service <https://vroncevic.github.io/gen_mqtt_service>`_

**gen_mqtt_service** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
