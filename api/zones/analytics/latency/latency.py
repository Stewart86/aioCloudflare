from api.commons.auth import Auth

from .colos.colos import Colos


class Latency(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "analytics/latency"
    _endpoint3 = None

    @property
    def colos(self):
        return Colos()
