from aiocloudflare.commons.auth import Auth


class AlwaysUseHttps(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/always_use_https"
    _endpoint3 = None
