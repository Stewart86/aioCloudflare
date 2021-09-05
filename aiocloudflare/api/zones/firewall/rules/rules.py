from aiocloudflare.commons.auth import Auth


class Rules(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/rules"
    _endpoint3 = None
