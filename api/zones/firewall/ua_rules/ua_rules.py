from api.commons.auth import Auth


class UaRules(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "firewall/ua_rules"
    _endpoint3 = None
