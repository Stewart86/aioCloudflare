from api.commons.auth import Auth


class Overrides(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf/overrides"
    _endpoint3 = None
