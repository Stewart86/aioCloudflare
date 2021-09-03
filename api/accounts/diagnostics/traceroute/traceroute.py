from api.commons.auth import Auth


class Traceroute(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "diagnostics/traceroute"
    _endpoint3 = None
