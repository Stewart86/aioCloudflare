from api.commons.auth import Auth


class SecondaryDns(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "secondary_dns"
    _endpoint3 = None
