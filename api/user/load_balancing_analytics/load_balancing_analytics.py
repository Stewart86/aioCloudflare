from api.commons.unused import Unused

from .events.events import Events


class LoadBalancingAnalytics(Unused):
    _AUTH = "VOID"
    _endpoint1 = "user/load_balancing_analytics"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def events(self):
        return Events()
