from aiocloudflare.commons.auth import Auth

from .diagnose.diagnose import Diagnose


class Railguns(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "railguns"
    _endpoint3 = None

    @property
    def diagnose(self) -> Diagnose:
        return Diagnose(self._config, self._session)
