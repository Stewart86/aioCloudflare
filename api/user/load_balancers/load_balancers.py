from api.commons.unused import Unused

from .monitors.monitors import Monitors
from .preview.preview import Preview
from .pools.pools import Pools


class LoadBalancers(Unused):
    _AUTH = "VOID"
    _endpoint1 = "user/load_balancers"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def monitors(self):
        return Monitors()

    @property
    def preview(self):
        return Preview()

    @property
    def pools(self):
        return Pools()
