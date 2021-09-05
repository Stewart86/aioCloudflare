from aiocloudflare.commons.auth import Auth


class Primaries(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "secondary_dns/primaries"
    _endpoint3 = None
