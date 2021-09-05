from aiocloudflare.commons.unused import Unused

from .exists.exists import Exists


class Destination(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "logpush/validate/destination"
    _endpoint3 = None

    @property
    def exists(self) -> Exists:
        return Exists(self._config, self._session)
