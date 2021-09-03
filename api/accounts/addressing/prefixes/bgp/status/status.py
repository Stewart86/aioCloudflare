from api.commons.auth import Auth


class Status(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "addressing/prefixes"
    _endpoint3 = "bgp/status"
