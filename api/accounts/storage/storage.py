from api.commons.unused import Unused

from .analytics.analytics import Analytics
from .kv.kv import Kv


class Storage(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "storage"
    _endpoint3 = None

    @property
    def analytics(self):
        return Analytics()

    @property
    def kv(self):
        return Kv()
