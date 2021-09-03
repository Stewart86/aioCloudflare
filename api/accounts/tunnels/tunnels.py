from api.commons.auth import Auth

from .connections.connections import Connections


class Tunnels(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "tunnels"
    _endpoint3 = None

    @property
    def connections(self):
        return Connections()
