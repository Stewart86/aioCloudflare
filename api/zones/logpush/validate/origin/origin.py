from api.commons.auth import Auth


class Origin(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "logpush/validate/origin"
    _endpoint3 = None
