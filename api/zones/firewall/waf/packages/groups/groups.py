from api.commons.auth import Auth


class Groups(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf/packages"
    _endpoint3 = "groups"
