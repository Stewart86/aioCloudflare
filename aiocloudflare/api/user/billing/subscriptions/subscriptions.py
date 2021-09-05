from aiocloudflare.commons.unused import Unused

from .apps.apps import Apps
from .zones.zones import Zones


class Subscriptions(Unused):
    _endpoint1 = "user/billing/subscriptions"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def apps(self) -> Apps:
        return Apps(self._config, self._session)

    @property
    def zones(self) -> Zones:
        return Zones(self._config, self._session)
