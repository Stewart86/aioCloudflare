from aiocloudflare.commons.auth import Auth


class MinTlsVersion(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/min_tls_version"
    _endpoint3 = None
