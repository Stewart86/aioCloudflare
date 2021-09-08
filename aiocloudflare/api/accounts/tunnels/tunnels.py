from aiocloudflare.commons.auth import Auth

from .connections.connections import Connections


class Tunnels(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "tunnels"
    _endpoint3 = None

    @property
    def connections(self) -> Connections:
        return Connections(self._config, self._session)
