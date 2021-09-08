from aiocloudflare.commons.auth import Auth

from .import_.import_ import Import_
from .versions.versions import Versions


class Rulesets(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "rulesets"
    _endpoint3 = None

    @property
    def versions(self) -> Versions:
        return Versions(self._config, self._session)

    @property
    def import_(self) -> Import_:
        return Import_(self._config, self._session)
