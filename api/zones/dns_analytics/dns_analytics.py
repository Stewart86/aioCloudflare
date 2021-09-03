from api.commons.unused import Unused

from .report.report import Report


class DnsAnalytics(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "dns_analytics"
    _endpoint3 = None

    @property
    def report(self):
        return Report()
