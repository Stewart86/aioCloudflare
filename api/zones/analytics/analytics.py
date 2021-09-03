from api.commons.unused import Unused

from .colos.colos import Colos
from .dashboard.dashboard import Dashboard
from .latency.latency import Latency


class Analytics(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "analytics"
    _endpoint3 = None

    @property
    def colos(self):
        return Colos()

    @property
    def dashboard(self):
        return Dashboard()

    @property
    def latency(self):
        return Latency()
