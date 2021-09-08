from aiocloudflare.commons.unused import Unused

from .colos.colos import Colos
from .dashboard.dashboard import Dashboard
from .latency.latency import Latency


class Analytics(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "analytics"
    _endpoint3 = None

    @property
    def dashboard(self) -> Dashboard:
        return Dashboard(self._config, self._session)

    @property
    def latency(self) -> Latency:
        return Latency(self._config, self._session)

    @property
    def colos(self) -> Colos:
        return Colos(self._config, self._session)
