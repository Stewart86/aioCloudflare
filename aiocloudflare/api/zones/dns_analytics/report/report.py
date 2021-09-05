from aiocloudflare.commons.auth import Auth

from .bytime.bytime import Bytime


class Report(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "dns_analytics/report"
    _endpoint3 = None

    @property
    def bytime(self) -> Bytime:
        return Bytime(self._config, self._session)
