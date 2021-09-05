from aiocloudflare.commons.auth import Auth

from .colos.colos import Colos


class Latency(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "analytics/latency"
    _endpoint3 = None

    @property
    def colos(self) -> Colos:
        return Colos(self._config, self._session)
