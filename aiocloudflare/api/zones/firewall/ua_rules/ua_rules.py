from aiocloudflare.commons.auth import Auth


class UaRules(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/ua_rules"
    _endpoint3 = None
