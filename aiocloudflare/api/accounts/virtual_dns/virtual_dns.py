from aiocloudflare.commons.auth import Auth


class VirtualDns(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "virtual_dns"
    _endpoint3 = None
