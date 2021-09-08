from aiocloudflare.commons.unused import Unused

from .analytics.analytics import Analytics
from .kv.kv import Kv


class Storage(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "storage"
    _endpoint3 = None

    @property
    def kv(self) -> Kv:
        return Kv(self._config, self._session)

    @property
    def analytics(self) -> Analytics:
        return Analytics(self._config, self._session)
