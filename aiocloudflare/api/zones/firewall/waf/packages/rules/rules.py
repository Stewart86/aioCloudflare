from aiocloudflare.commons.auth import Auth


class Rules(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf/packages"
    _endpoint3 = "rules"
