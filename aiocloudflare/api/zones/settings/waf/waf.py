from aiocloudflare.commons.auth import Auth


class Waf(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/waf"
    _endpoint3 = None
