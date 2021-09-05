from aiocloudflare.commons.auth import Auth


class Brotli(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/brotli"
    _endpoint3 = None
