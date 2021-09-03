from api.commons.auth import Auth


class MinTlsVersion(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/min_tls_version"
    _endpoint3 = None
