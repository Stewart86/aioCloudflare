from aiocloudflare.commons.auth import Auth

from .dns_analytics.dns_analytics import DnsAnalytics


class VirtualDns(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "virtual_dns"
    _endpoint3 = None

    @property
    def dns_analytics(self) -> DnsAnalytics:
        return DnsAnalytics(self._config, self._session)
