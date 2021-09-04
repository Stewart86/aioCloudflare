from api.commons.unused import Unused

from .exists.exists import Exists


class Destination(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "logpush/validate/destination"
    _endpoint3 = None

    @property
    def exists(self):
        return Exists(self._config, self._session)
