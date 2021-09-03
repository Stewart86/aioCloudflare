from api.commons.auth import Auth


class Jobs(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "logpush/jobs"
    _endpoint3 = None
