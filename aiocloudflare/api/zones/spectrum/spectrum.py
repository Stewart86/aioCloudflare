from aiocloudflare.commons.unused import Unused

from .analytics.analytics import Analytics
from .apps.apps import Apps


class Spectrum(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "spectrum"
    _endpoint3 = None

    @property
    def apps(self) -> Apps:
        return Apps(self._config, self._session)

    @property
    def analytics(self) -> Analytics:
        return Analytics(self._config, self._session)
