from api.commons.auth import Auth

from .bindings.bindings import Bindings


class Script(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "workers/script"
    _endpoint3 = None

    @property
    def bindings(self):
        return Bindings()
