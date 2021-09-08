from aiocloudflare.commons.unused import Unused

from .sxg.sxg import Sxg


class Amp(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "amp"
    _endpoint3 = None

    @property
    def sxg(self) -> Sxg:
        return Sxg(self._config, self._session)
