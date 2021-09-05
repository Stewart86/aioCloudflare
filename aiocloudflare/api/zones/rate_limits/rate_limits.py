from aiocloudflare.commons.auth import Auth


class RateLimits(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "rate_limits"
    _endpoint3 = None
