from api.commons.unused import Unused

from .current.current import Current


class Aggregate(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics/aggregate"
    _endpoint3 = None

    @property
    def current(self):
        return Current()
