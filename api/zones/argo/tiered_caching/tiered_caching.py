from api.commons.auth import Auth


class TieredCaching(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "argo/tiered_caching"
    _endpoint3 = None
