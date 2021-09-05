from aiocloudflare.commons.auth import Auth


class Stored(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "storage/analytics/stored"
    _endpoint3 = None
