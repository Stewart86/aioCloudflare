from aiocloudflare.commons.auth import Auth


class BrowserCacheTtl(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/browser_cache_ttl"
    _endpoint3 = None
