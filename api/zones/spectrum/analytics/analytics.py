from api.commons.unused import Unused

from .aggregate.aggregate import Aggregate
from .events.events import Events


class Analytics(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics"
    _endpoint3 = None

    @property
    def aggregate(self):
        return Aggregate(self._config, self._session)

    @property
    def events(self):
        return Events(self._config, self._session)
