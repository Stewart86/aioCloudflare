from api.commons.auth import Auth


class Verification(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "ssl/verification"
    _endpoint3 = None
