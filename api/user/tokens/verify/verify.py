from api.commons.auth import Auth


class Verify(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/tokens/verify"
    _endpoint2 = None
    _endpoint3 = None
