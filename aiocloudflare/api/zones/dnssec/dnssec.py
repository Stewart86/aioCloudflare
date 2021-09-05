from aiocloudflare.commons.auth import Auth


class Dnssec(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "dnssec"
    _endpoint3 = None
