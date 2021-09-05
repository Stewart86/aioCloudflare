from aiocloudflare.commons.unused import Unused

from .report.report import Report


class DnsAnalytics(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "virtual_dns"
    _endpoint3 = "dns_analytics"

    @property
    def report(self) -> Report:
        return Report(self._config, self._session)
