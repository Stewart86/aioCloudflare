from api.commons.unused import Unused

from .preview.preview import Preview
from .monitors.monitors import Monitors
from .pools.pools import Pools
from .regions.regions import Regions
from .search.search import Search


class LoadBalancers(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers"
    _endpoint3 = None

    @property
    def preview(self):
        return Preview()

    @property
    def monitors(self):
        return Monitors()

    @property
    def pools(self):
        return Pools()

    @property
    def regions(self):
        return Regions()

    @property
    def search(self):
        return Search()
