from api.commons.unused import Unused

from .report.report import Report


class DnsAnalytics(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "virtual_dns"
    _endpoint3 = "dns_analytics"

    @property
    def report(self):
        return Report()
