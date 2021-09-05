from aiocloudflare.commons.auth import Auth


class Overrides(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf/overrides"
    _endpoint3 = None
