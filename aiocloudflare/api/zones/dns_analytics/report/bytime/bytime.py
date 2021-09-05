from aiocloudflare.commons.auth import Auth


class Bytime(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "dns_analytics/report/bytime"
    _endpoint3 = None
