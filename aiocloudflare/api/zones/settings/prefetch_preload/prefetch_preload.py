from aiocloudflare.commons.auth import Auth


class PrefetchPreload(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/prefetch_preload"
    _endpoint3 = None
