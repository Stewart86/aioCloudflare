from api.commons.auth import Auth

from .versions.versions import Versions


class Rulesets(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "rulesets"
    _endpoint3 = None

    @property
    def versions(self):
        return Versions()
