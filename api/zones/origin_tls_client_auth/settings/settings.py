from api.commons.auth import Auth


class Settings(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "origin_tls_client_auth/settings"
    _endpoint3 = None
