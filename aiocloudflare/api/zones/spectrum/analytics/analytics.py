from aiocloudflare.commons.unused import Unused

from .aggregate.aggregate import Aggregate
from .events.events import Events


class Analytics(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics"
    _endpoint3 = None

    @property
    def aggregate(self) -> Aggregate:
        return Aggregate(self._config, self._session)

    @property
    def events(self) -> Events:
        return Events(self._config, self._session)
