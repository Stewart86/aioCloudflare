aioCloudflare
=============

|PyPI| |Status| |Python Version| |License|

|Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/aiocloudflare.svg
   :target: https://pypi.org/project/aiocloudflare/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/aiocloudflare.svg
   :target: https://pypi.org/project/aiocloudflare/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/aiocloudflare
   :target: https://pypi.org/project/aiocloudflare
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/aiocloudflare
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Tests| image:: https://github.com/stewart86/aiocloudflare/workflows/Tests/badge.svg
   :target: https://github.com/stewart86/aiocloudflare/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/stewart86/aiocloudflare/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/stewart86/aiocloudflare
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

* async http API call using modern http library ``httpx``.
* Autocompletion on IDE.
* Fully type hinted.


Requirements
------------

* ``Python`` 3.9+


Installation
------------

You can install *aiocloudflare* via pip_ from PyPI_:

.. code:: console

   $ pip install aiocloudflare


Usage
-----

.. code:: Python

    from aiocloudflare import Cloudflare

    async def get_zone():
        async with Cloudflare() as cf:
            result = await cf.zones.get()


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `MIT license`_,
*Hello World* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _file an issue: https://github.com/stewart86/aiocloudflare/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
