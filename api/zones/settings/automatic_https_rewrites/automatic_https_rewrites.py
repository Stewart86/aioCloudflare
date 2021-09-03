from api.commons.auth import Auth


class AutomaticHttpsRewrites(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/automatic_https_rewrites"
    _endpoint3 = None
