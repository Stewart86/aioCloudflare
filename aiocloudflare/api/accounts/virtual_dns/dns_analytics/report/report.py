from aiocloudflare.commons.auth import Auth

from .bytime.bytime import Bytime


class Report(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "virtual_dns"
    _endpoint3 = "dns_analytics/report"

    @property
    def bytime(self) -> Bytime:
        return Bytime(self._config, self._session)
