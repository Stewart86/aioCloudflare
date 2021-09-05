from aiocloudflare.commons.auth import Auth


class PurgeCache(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "purge_cache"
    _endpoint3 = None
