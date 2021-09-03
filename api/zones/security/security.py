from api.commons.unused import Unused

from .events.events import Events


class Security(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "security"
    _endpoint3 = None

    @property
    def events(self):
        return Events()
