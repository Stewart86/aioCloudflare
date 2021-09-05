from aiocloudflare.commons.auth import Auth


class MobileRedirect(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/mobile_redirect"
    _endpoint3 = None
