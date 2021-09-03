from api.commons.unused import Unused

from .analytics.analytics import Analytics
from .apps.apps import Apps


class Spectrum(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "spectrum"
    _endpoint3 = None

    @property
    def analytics(self):
        return Analytics()

    @property
    def apps(self):
        return Apps()
