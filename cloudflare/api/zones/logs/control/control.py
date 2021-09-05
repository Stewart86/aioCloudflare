from cloudflare.commons.auth import Auth

from .retention.retention import Retention


class Control(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "logs/control"
    _endpoint3 = None

    @property
    def retention(self):
        return Retention(self._config, self._session)
