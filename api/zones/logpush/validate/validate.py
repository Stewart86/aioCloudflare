from api.commons.unused import Unused

from .destination.destination import Destination
from .origin.origin import Origin


class Validate(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "logpush/validate"
    _endpoint3 = None

    @property
    def destination(self):
        return Destination(self._config, self._session)

    @property
    def origin(self):
        return Origin(self._config, self._session)
