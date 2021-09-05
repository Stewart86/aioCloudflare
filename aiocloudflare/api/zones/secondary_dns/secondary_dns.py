from aiocloudflare.commons.auth import Auth


class SecondaryDns(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "secondary_dns"
    _endpoint3 = None
