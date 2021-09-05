from aiocloudflare.commons.auth import Auth


class PseudoIpv4(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/pseudo_ipv4"
    _endpoint3 = None
