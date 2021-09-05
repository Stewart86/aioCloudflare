from aiocloudflare.commons.auth import Auth


class CacheLevel(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/cache_level"
    _endpoint3 = None
