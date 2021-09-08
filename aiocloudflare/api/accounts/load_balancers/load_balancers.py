from aiocloudflare.commons.unused import Unused

from .monitors.monitors import Monitors
from .pools.pools import Pools
from .preview.preview import Preview
from .regions.regions import Regions
from .search.search import Search


class LoadBalancers(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers"
    _endpoint3 = None

    @property
    def search(self) -> Search:
        return Search(self._config, self._session)

    @property
    def pools(self) -> Pools:
        return Pools(self._config, self._session)

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)

    @property
    def monitors(self) -> Monitors:
        return Monitors(self._config, self._session)

    @property
    def regions(self) -> Regions:
        return Regions(self._config, self._session)
