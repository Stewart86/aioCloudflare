from api.commons.auth import Auth


class Rules(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "firewall/access_rules/rules"
    _endpoint3 = None
