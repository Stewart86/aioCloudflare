from api.commons.auth import Auth


class Exists(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "logpush/validate/destination/exists"
    _endpoint3 = None
