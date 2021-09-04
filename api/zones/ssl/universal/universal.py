from api.commons.unused import Unused

from .settings.settings import Settings


class Universal(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "ssl/universal"
    _endpoint3 = None

    @property
    def settings(self):
        return Settings(self._config, self._session)
