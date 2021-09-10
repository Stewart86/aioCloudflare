aioCloudflare
=============

|PyPI| |Status| |Python Version| |License|

|Tests| |Codecov|

|pre-commit| |Black|

|Downloads|

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
.. |Downloads| image:: https://static.pepy.tech/badge/aiocloudflare
   :target: https://pepy.tech/project/aiocloudflare
   :alt: Downloads

Inspired by the offical ``python-cloudflare`` library developed by `Cloudflare`_. This project is created to be compatible with ``asyncio`` for non-blocking IO.

For sync code, it is recommanded to use ``python-cloudflare`` via ``pip install python-cloudflare`` as it is used by hundreds and offically maintained by Cloudflare. This ensure that APIs are always updated according to Cloudflare API release.

*NOTE:* This library is in Beta, this means fixes and updates are still going on every second. Do not use it in Production unless you have tested on the API route specific to your use case and that would be at your own risk.

Having said that, do submit an issue if you encounter any bug so we can move away from the Alpha stage sooner.

Features
--------

* async http API call using modern http library ``httpx``.
* Autocompletion on IDE.
* Fully type hinted.

Feature Roadmap
---------------

* to support cert token
* to support sync API client

These are some alternative use cases that are not in the top of my priority now as I have not received
any request for. If you are interested, you may want to submit a pull request to contribute some of these features.


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
            response = await cf.zones.get()

Unlike the offical ``python-cloudflare`` library, ``aiocloudflare`` does not parse and handle http responses.

So the awaited response object will have to be handled just as any http request, response pattern. the ``Response`` object is the same as ``httpx``'s ``Response``.

.. code:: Python

    from aiocloudflare import Cloudflare

    async def get_zone():
        async with Cloudflare() as cf:
            response = await cf.zones.get()

            # check status code
            if response.status_code == 200:

                # get json data
                resp_json = response.json()

                # Cloudflare API typically store results in a ``result`` key.
                return resp_json["result"]

            else:
                # to get texture data from response
                print(response.text)


Full configuration can be done using ``Config()`` class.

.. code:: Python

    from aioCloudflare import Cloudflare, Config

    config = Config(email="your@email.com", token="<secret>")  # for demo only, do not hardcode secrets
    async def get_zone():
        async with Cloudflare(config=config) as cf:
            result = await cf.zones.get()

Configuration can also be stored in a ``.env`` file for a "global" configuration without needing to create a ``Config()`` class. Keys available are:

.. code:: console

    CF_API_EMAIL=""
    CF_API_KEY=""
    CF_API_CERTKEY=""
    CF_API_URL=""
    DEBUG=false
    CF_PROFILE=""
    USER_AGENT=""

Advance Usage
_____________

You may wish to wrap ``Cloudflare()`` into you own class for customised settings or requirements. To do that, just provide a ``__aenter__()`` and ``__aexit__()`` method to your class like so.

.. code:: Python

    class MyCfClient:
        def __init__(self):
            self._config = Config(email="your@email.com", token="<secret>")  # for demo only, do not hardcode secrets

        async def __aenter__(self):
            self._client = Cloudflare(config=self._config)
            return self

        async def __aexit__(self, exc_type, exc_value, traceback):
            await self._client.aclose()

Then you can call your own class with async context manager.

.. code:: Python

    async with MyCfClient() as own_class:
        await own_class.zones.get()


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `MIT license`_,
*aioCloudflare* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _file an issue: https://github.com/stewart86/aiocloudflare/issues
.. _pip: https://pip.pypa.io/
.. _Cloudflare: https://github.com/cloudflare/python-cloudflare
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
