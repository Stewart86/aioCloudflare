from api.commons.auth import Auth


class Ssl(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/ssl"
    _endpoint3 = None
