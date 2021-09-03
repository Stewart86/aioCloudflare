from api.commons.auth import Auth

from .force_axfr.force_axfr import ForceAxfr


class SecondaryDns(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "secondary_dns"
    _endpoint3 = None

    @property
    def force_axfr(self):
        return ForceAxfr()
