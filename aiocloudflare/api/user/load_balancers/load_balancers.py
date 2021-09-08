from aiocloudflare.commons.unused import Unused

from .monitors.monitors import Monitors
from .pools.pools import Pools
from .preview.preview import Preview


class LoadBalancers(Unused):
    _endpoint1 = "user/load_balancers"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def pools(self) -> Pools:
        return Pools(self._config, self._session)

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)

    @property
    def monitors(self) -> Monitors:
        return Monitors(self._config, self._session)
