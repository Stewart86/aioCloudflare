from api.commons.auth import Auth


class Dnssec(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "dnssec"
    _endpoint3 = None
