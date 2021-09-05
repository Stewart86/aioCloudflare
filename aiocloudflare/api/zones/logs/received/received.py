from aiocloudflare.commons.auth_unwrapped import AuthUnwrapped

from .fields.fields import Fields


class Received(AuthUnwrapped):
    _endpoint1 = "zones"
    _endpoint2 = "logs/received"
    _endpoint3 = None

    @property
    def fields(self) -> Fields:
        return Fields(self._config, self._session)
