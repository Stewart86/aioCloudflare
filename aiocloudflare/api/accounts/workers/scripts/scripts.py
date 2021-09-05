from aiocloudflare.commons.auth import Auth

from .schedules.schedules import Schedules


class Scripts(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "workers/scripts"
    _endpoint3 = None

    @property
    def schedules(self) -> Schedules:
        return Schedules(self._config, self._session)
