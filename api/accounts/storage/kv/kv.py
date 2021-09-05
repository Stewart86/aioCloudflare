from api.commons.unused import Unused

from .namespaces.namespaces import Namespaces


class Kv(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "storage/kv"
    _endpoint3 = None

    @property
    def namespaces(self):
        return Namespaces(self._config, self._session)
