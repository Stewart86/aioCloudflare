from aiocloudflare.commons.auth import Auth


class FallbackOrigin(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "custom_hostnames/fallback_origin"
    _endpoint3 = None
