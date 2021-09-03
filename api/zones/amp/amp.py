from api.commons.unused import Unused

from .sxg.sxg import Sxg


class Amp(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "amp"
    _endpoint3 = None

    @property
    def sxg(self):
        return Sxg()
