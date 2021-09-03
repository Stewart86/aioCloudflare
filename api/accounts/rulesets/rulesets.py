from api.commons.auth import Auth

from .versions.versions import Versions
from .import_.import_ import Import_


class Rulesets(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "rulesets"
    _endpoint3 = None

    @property
    def versions(self):
        return Versions()

    @property
    def import_(self):
        return Import_()
