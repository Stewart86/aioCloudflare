from aiocloudflare.commons.auth import Auth


class Validate(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "logpush/ownership/validate"
    _endpoint3 = None
