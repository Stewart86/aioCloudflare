from aiocloudflare.commons.unused import Unused

from .events.events import Events


class LoadBalancingAnalytics(Unused):
    _endpoint1 = "user/load_balancing_analytics"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def events(self) -> Events:
        return Events(self._config, self._session)
