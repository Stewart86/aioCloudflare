from api.commons.auth import Auth

from .bulk.bulk import Bulk
from .keys.keys import Keys
from .values.values import Values


class Namespaces(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "storage/kv/namespaces"
    _endpoint3 = None

    @property
    def bulk(self):
        return Bulk(self._config, self._session)

    @property
    def keys(self):
        return Keys(self._config, self._session)

    @property
    def values(self):
        return Values(self._config, self._session)
