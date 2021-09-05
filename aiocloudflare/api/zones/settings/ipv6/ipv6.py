from aiocloudflare.commons.auth import Auth


class Ipv6(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/ipv6"
    _endpoint3 = None
