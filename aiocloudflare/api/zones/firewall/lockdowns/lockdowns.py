from aiocloudflare.commons.auth import Auth


class Lockdowns(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/lockdowns"
    _endpoint3 = None
