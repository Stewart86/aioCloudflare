from api.commons.auth import Auth


class Preview(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "stream/preview"
    _endpoint3 = None
