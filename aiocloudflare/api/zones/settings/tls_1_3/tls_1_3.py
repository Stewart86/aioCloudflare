from aiocloudflare.commons.auth import Auth


class Tls13(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/tls_1_3"
    _endpoint3 = None
