from aiocloudflare.commons.auth import Auth

from .force_axfr.force_axfr import ForceAxfr


class SecondaryDns(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "secondary_dns"
    _endpoint3 = None

    @property
    def force_axfr(self) -> ForceAxfr:
        return ForceAxfr(self._config, self._session)
