from api.commons.auth import Auth


class Colos(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "analytics/latency/colos"
    _endpoint3 = None
