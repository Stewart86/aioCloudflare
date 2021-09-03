from api.commons.auth import Auth


class Lockdowns(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "firewall/lockdowns"
    _endpoint3 = None
