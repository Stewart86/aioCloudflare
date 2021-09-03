from api.commons.auth import Auth


class Rules(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/firewall/access_rules/rules"
    _endpoint2 = None
    _endpoint3 = None
