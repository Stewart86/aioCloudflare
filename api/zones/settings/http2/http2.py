from api.commons.auth import Auth


class Http2(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/http2"
    _endpoint3 = None
