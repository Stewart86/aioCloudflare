from aiocloudflare.commons.auth import Auth

from .validate.validate import Validate


class Ownership(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "logpush/ownership"
    _endpoint3 = None

    @property
    def validate(self) -> Validate:
        return Validate(self._config, self._session)
