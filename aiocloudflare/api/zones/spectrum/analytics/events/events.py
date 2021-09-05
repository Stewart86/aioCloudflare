from aiocloudflare.commons.unused import Unused

from .bytime.bytime import Bytime
from .summary.summary import Summary


class Events(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics/events"
    _endpoint3 = None

    @property
    def bytime(self) -> Bytime:
        return Bytime(self._config, self._session)

    @property
    def summary(self) -> Summary:
        return Summary(self._config, self._session)
