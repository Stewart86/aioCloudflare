from api.commons.auth import Auth


class RateLimits(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "rate_limits"
    _endpoint3 = None
