from aiocloudflare.commons.unused import Unused

from .current.current import Current


class Aggregate(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics/aggregate"
    _endpoint3 = None

    @property
    def current(self) -> Current:
        return Current(self._config, self._session)
