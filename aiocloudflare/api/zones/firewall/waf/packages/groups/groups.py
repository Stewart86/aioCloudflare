from aiocloudflare.commons.auth import Auth


class Groups(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf/packages"
    _endpoint3 = "groups"
