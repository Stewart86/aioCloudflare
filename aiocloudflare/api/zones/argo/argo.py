from aiocloudflare.commons.unused import Unused

from .smart_routing.smart_routing import SmartRouting
from .tiered_caching.tiered_caching import TieredCaching


class Argo(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "argo"
    _endpoint3 = None

    @property
    def smart_routing(self) -> SmartRouting:
        return SmartRouting(self._config, self._session)

    @property
    def tiered_caching(self) -> TieredCaching:
        return TieredCaching(self._config, self._session)
