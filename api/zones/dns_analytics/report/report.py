from api.commons.auth import Auth

from .bytime.bytime import Bytime


class Report(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "dns_analytics/report"
    _endpoint3 = None

    @property
    def bytime(self):
        return Bytime()
