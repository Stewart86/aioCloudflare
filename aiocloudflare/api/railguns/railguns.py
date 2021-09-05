from aiocloudflare.commons.auth import Auth

from .zones.zones import Zones


class Railguns(Auth):
    _endpoint1 = "railguns"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def zones(self) -> Zones:
        return Zones(self._config, self._session)
