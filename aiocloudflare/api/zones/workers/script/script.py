from aiocloudflare.commons.auth import Auth

from .bindings.bindings import Bindings


class Script(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "workers/script"
    _endpoint3 = None

    @property
    def bindings(self) -> Bindings:
        return Bindings(self._config, self._session)
