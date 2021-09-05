from aiocloudflare.commons.auth import Auth


class OriginTlsClientAuth(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "origin_tls_client_auth"
    _endpoint3 = None
