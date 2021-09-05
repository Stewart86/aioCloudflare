from cloudflare.commons.unused import Unused

from .apps.apps import Apps
from .zones.zones import Zones


class Subscriptions(Unused):
    _endpoint1 = "user/billing/subscriptions"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def apps(self):
        return Apps(self._config, self._session)

    @property
    def zones(self):
        return Zones(self._config, self._session)
