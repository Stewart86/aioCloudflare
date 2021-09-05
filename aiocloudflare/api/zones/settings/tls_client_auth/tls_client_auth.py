from aiocloudflare.commons.auth import Auth


class TlsClientAuth(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/tls_client_auth"
    _endpoint3 = None
