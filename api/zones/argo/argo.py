from api.commons.unused import Unused

from .tiered_caching.tiered_caching import TieredCaching
from .smart_routing.smart_routing import SmartRouting


class Argo(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "argo"
    _endpoint3 = None

    @property
    def tiered_caching(self):
        return TieredCaching()

    @property
    def smart_routing(self):
        return SmartRouting()
