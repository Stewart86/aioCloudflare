from api.commons.auth import Auth


class Ipv6(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/ipv6"
    _endpoint3 = None
