from api.commons.auth import Auth


class Copy(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "stream/copy"
    _endpoint3 = None
