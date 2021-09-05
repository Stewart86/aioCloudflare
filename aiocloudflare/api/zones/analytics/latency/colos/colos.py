from aiocloudflare.commons.auth import Auth


class Colos(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "analytics/latency/colos"
    _endpoint3 = None
