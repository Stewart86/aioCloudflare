from api.commons.auth import Auth


class VirtualDns(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "virtual_dns"
    _endpoint3 = None
