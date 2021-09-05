from aiocloudflare.commons.auth import Auth


class ForceAxfr(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "secondary_dns/force_axfr"
    _endpoint3 = None
