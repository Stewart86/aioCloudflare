from aiocloudflare.commons.auth import Auth

from .versions.versions import Versions


class Rulesets(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "rulesets"
    _endpoint3 = None

    @property
    def versions(self) -> Versions:
        return Versions(self._config, self._session)
