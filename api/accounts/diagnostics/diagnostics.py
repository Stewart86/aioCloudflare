from api.commons.unused import Unused

from .traceroute.traceroute import Traceroute


class Diagnostics(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "diagnostics"
    _endpoint3 = None

    @property
    def traceroute(self):
        return Traceroute()
