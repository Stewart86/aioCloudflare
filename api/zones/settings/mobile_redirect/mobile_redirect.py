from api.commons.auth import Auth


class MobileRedirect(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/mobile_redirect"
    _endpoint3 = None
