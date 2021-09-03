from api.commons.unused import Unused

from .bytime.bytime import Bytime
from .summary.summary import Summary


class Events(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics/events"
    _endpoint3 = None

    @property
    def bytime(self):
        return Bytime()

    @property
    def summary(self):
        return Summary()
