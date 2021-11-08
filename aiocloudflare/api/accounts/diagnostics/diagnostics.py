from aiocloudflare.commons.unused import Unused

from .traceroute.traceroute import Traceroute


class Diagnostics(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "diagnostics"
    _endpoint3 = None

    @property
    def traceroute(self) -> Traceroute:
        return Traceroute(self._config, self._session)
