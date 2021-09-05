from aiocloudflare.commons.auth import Auth


class Origin(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "logpush/validate/origin"
    _endpoint3 = None
