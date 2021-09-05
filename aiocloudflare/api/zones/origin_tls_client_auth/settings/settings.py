from aiocloudflare.commons.auth import Auth


class Settings(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "origin_tls_client_auth/settings"
    _endpoint3 = None
